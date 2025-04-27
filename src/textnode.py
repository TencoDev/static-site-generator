from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
        
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    
def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type not in TextType:
        raise Exception("Not a valid text type!")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value = text_node.text, props=None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", value=None, props={"src": text_node.url, "alt":text_node.text })