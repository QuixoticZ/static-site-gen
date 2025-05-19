from enum import Enum
import re
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node,TextNode,TextType
from htmlnode import *


class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def markdown_to_blocks(markdown):
    blocks=markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if re.match(r"^#{1,6}\s",block):
        return BlockType.HEADING
    if re.match(r"^`{3}[\s\S]+`{3}",block):
        return BlockType.CODE
    if re.match(r"(?m)^>.+",block):
        return BlockType.QUOTE
    if re.match(r"(?m)^- .+",block):
        return BlockType.UNORDERED_LIST
    lines=block.split("\n")
    line_count=1
    for line in lines:
        if re.match(rf"^{line_count}\. .+",line):
            line_count +=1
    if line_count-1 == len(lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    text_nodes=text_to_textnodes(text)
    html_nodes=[]
    for node in text_nodes:
        html_node=text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes

def list_rows(block):
    pass
    
def block_to_html_node_heading(block):
    header_hash = re.findall(r"#",block)
    header_type = len(header_hash)
    string_text=block[header_type+1:]
    new_parent=ParentNode(f"h{header_type}",text_to_children(string_text))
    return new_parent

def block_to_html_node_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    new_parent=ParentNode(f"blockquote",text_to_children(children))
    return new_parent

def block_to_html_node_unordered_list(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("ul", children))
    new_parent=ParentNode("ol",text_to_children(html_items))
    return new_parent

def block_to_html_node_ordered_list(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    new_parent=ParentNode("ol",text_to_children(html_items))
    return new_parent

def block_to_html_node_code(block):
    code_node=TextNode(block,TextType.CODE)
    new_parent=ParentNode("code",text_node_to_html_node(code_node))
    return new_parent

def block_to_html_node_paragraph(block):
    lines = block.split("\n")
    paragraph=" ".join(lines)
    new_parent=ParentNode("p",text_to_children(paragraph))
    return new_parent

def markdown_to_html_node(markdown):
    blocks=markdown_to_blocks(markdown)
    child_nodes=[]
    for block in blocks:
        block_type=block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                child_nodes.append(block_to_html_node_heading(block))
            case BlockType.QUOTE:
                child_nodes.append(block_to_html_node_quote(block))
            case BlockType.UNORDERED_LIST:
                child_nodes.append(block_to_html_node_unordered_list(block))
            case BlockType.ORDERED_LIST:
                child_nodes.append(block_to_html_node_ordered_list(block))
            case BlockType.CODE:
                child_nodes.append(block_to_html_node_code(block))
            case BlockType.PARAGRAPH:
                child_nodes.append(block_to_html_node_paragraph(block))
    block_parent=ParentNode("div",child_nodes)
    return block_parent
            
    
        