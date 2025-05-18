from enum import Enum
import re

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

