from textnode import TextNode,TextType
import re




def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        found_images = extract_markdown_images(old_node.text)
        original_text = old_node.text
        if len(found_images) == 0:
            new_nodes.append(old_node)
            continue
        for image_alt, image_url in found_images:
            sections = original_text.split(f"![{image_alt}]({image_url})",1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(image_alt,TextType.IMAGE,image_url))
            original_text = sections[1]
        if original_text != "":
            split_nodes.append(TextNode(original_text,TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        found_links = extract_markdown_links(old_node.text)
        original_text = old_node.text
        if len(found_links) == 0:
            new_nodes.append(old_node)
            continue
        for link_text, link_url in found_links:
            sections = original_text.split(f"[{link_text}]({link_url})",1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(link_text,TextType.LINK,link_url))
            original_text = sections[1]
        if original_text != "":
            split_nodes.append(TextNode(original_text,TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    working_nodes = [TextNode(text, TextType.TEXT)]
    working_nodes = split_nodes_delimiter(working_nodes,"**",TextType.BOLD)
    working_nodes = split_nodes_delimiter(working_nodes,"_",TextType.ITALIC)
    working_nodes = split_nodes_delimiter(working_nodes,"`",TextType.CODE)
    working_nodes = split_nodes_image(working_nodes)
    working_nodes = split_nodes_link(working_nodes)
    return working_nodes