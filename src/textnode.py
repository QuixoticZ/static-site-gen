from enum import Enum

from htmlnode import *

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text   
        self.text_type = text_type
        self.url = url

    def __eq__(self,otherTextNode):
        if self.text == otherTextNode.text and self.text_type == otherTextNode.text_type and self.url==otherTextNode.url:
            return True
        return False

    def __repr__(self):
        text_representation = f"TextNode({self.text}, {self.text_type}, {self.url})"
        return text_representation
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case text_node.text_type.TEXT:
            return LeafNode(None,text_node.text)
        case text_node.text_type.BOLD:
            return LeafNode("b",text_node.text)
        case text_node.text_type.ITALIC:
            return LeafNode("i",text_node.text)
        case text_node.text_type.CODE:
            return LeafNode("code",text_node.text)
        case text_node.text_type.LINK:
            return LeafNode("a",text_node.text,{"href":text_node.url})
        case text_node.text_type.IMAGE:
            return LeafNode("img",'',{"src":text_node.url,"alt":text_node.text})
        case _:
            raise Exception(f"invalid Text Type: {text_node.text_type}")

    