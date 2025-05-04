print("# hello world")
from textnode import TextNode 
from htmlnode import HTMLNode,LeafNode,ParentNode


def main():
    print("in main")
    testTextNode = TextNode("This is some anchor text","link","https://www.boot.dev")
    text_rept = testTextNode.__repr__
    print(text_rept)
    return None


main()