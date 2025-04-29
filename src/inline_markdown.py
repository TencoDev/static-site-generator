from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) % 2 == 0:
            new_nodes.append(node)
            continue

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

def extract_markdown_images(text):
   pattern = r"!\[([^\]]+)\]\(([^)]+)\)"
   matches = re.findall(pattern, text)
   return matches

def extract_markdown_links(text):
    pattern = r"\[([^\]]+)\]\(([^\)]+)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(text)
        
        if not matches:
            new_nodes.append(node)
            continue
        
        while matches:
            alt_text, img_link = matches[0]
            split_parts = text.split(f"![{alt_text}]({img_link})", 1)
            
            if split_parts[0]:
                new_nodes.append(TextNode(split_parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_link))
            
            text = split_parts[1]
            matches = extract_markdown_images(text)
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(text)
        
        if not matches:
            new_nodes.append(node)
            continue
        
        while matches:
            anchor_text, url = matches[0]
            split_parts = text.split(f"[{anchor_text}]({url})", 1)
            
            if split_parts[0]:
                new_nodes.append(TextNode(split_parts[0], TextType.TEXT))
            
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            
            text = split_parts[1]
            matches = extract_markdown_links(text)
        
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    
    return new_nodes 

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)

    return nodes
    
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

    
                 