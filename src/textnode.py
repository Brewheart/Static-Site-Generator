from enum import Enum
from htmlnode import HTMLNode, LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        node = LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        node = LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        node = LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        node = LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        node = LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        node = LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Invalid text type")
    return node

