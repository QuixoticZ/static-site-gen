import unittest
from block_markdown import *

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )


        
    def test_block_type_heading(self):
        block="#### TEST"
        block_result=block_to_block_type(block)
        
        self.assertEqual(block_result,BlockType.HEADING)

    def test_block_type_code(self):
        block="```TEST```"
        block_result=block_to_block_type(block)
        self.assertEqual(block_result,BlockType.CODE)

    def test_block_type_quote(self):
        block="""> test\n> example"""
        block_result=block_to_block_type(block)
        self.assertEqual(block_result,BlockType.QUOTE)

    def test_block_type_unordered_list(self):
        block="""- item1
- item2
- item3
"""
        block_result=block_to_block_type(block)
        self.assertEqual(block_result,BlockType.UNORDERED_LIST)

    def test_block_type_ordered_list(self):
        block="1. item1\n2. item2\n3. item3"
        block_result=block_to_block_type(block)  
        self.assertEqual(block_result,BlockType.ORDERED_LIST)

    def test_block_type_paragraph(self):
        print("Testrunning")
        block="1 item1\nA item2\n# item"
        block_result=block_to_block_type(block)
        self.assertEqual(block_result,BlockType.PARAGRAPH)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()