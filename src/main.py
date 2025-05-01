from textnode import *
from blocks import *
from inline_markdown import *
import os, shutil, sys

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return olist_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ulist_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        line = line.strip()
        if line:
            if not line.startswith(">"):
                raise ValueError("invalid quote block")
            new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def copy_to_destination(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    copy_recursively_src(src, dest)
    
def copy_recursively_src(src, dest):
    src_list = os.listdir(src)
    for src_asset in src_list:
        src_path = os.path.join(src, src_asset)
        if os.path.isfile(src_path):
            dest_path = os.path.join(dest, src_asset)
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} to {dest_path}")
        elif os.path.isdir(src_path):
            dest_path = os.path.join(dest, src_asset)
            os.mkdir(dest_path)
            print(f"Created directory: {dest_path}")
            copy_recursively_src(src_path, dest_path)
            
def extract_title(markdown):
    md_lines = markdown.splitlines()                
    for line in md_lines:
        if line.startswith("# "):
            text = line[2:].strip()
            return text
    raise Exception("No title found")
 

def read_file(file_path):
    file_path = str(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_file(content, dest_path):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(content)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown_content = read_file(from_path)
    template_content = read_file(template_path)

    title = extract_title(markdown_content)
    
    try:
        html_node = markdown_to_html_node(markdown_content)
        html_content = html_node.to_html()
    except ValueError as e:
        print("Error converting markdown to HTML:", e)
    
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    write_file(final_html, dest_path)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_list = os.listdir(dir_path_content)
    for content in content_list:
        file_path = os.path.join(dir_path_content, content)
        if os.path.isfile(file_path):
            if content.endswith('.md'):
                new_filename = content[:-3] + '.html'
                dest_path = os.path.join(dest_dir_path, new_filename)
            else:
                dest_path = os.path.join(dest_dir_path, content)
            generate_page(file_path, template_path, dest_path, basepath )
            print(f"Created file: {dest_path}")
            
        if os.path.isdir(file_path):
            dest_path = os.path.join(dest_dir_path, content)
            os.makedirs(dest_path, exist_ok=True)
            print(f"Created directory: {dest_path}")
            generate_pages_recursive(file_path, template_path, dest_path, basepath)
    
def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    copy_to_destination("static", "docs")
    generate_pages_recursive("content/", "template.html", "docs/", basepath)
    

if __name__ == "__main__":
    main()