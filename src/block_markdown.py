from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def markdown_to_blocks(markdown):
    markdown_blocks=markdown.strip().split("\n\n")
    blocks = [item for item in markdown_blocks if item]
    return blocks

def block_to_block_type(block):
    pass

