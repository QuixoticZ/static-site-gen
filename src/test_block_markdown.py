import unittest
from block_markdown import *
from copystatic import extract_title

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

    def test_block_to_html_heading(self):
        md = "#### test"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><h4>test</h4></div>")

    def test_block_to_html_quote(self):
        md = "> test\n> example"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><blockquote>test example</blockquote></div>")
    

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_extract_title(self):
        md ="#     Hello  "
        header = extract_title(md)
        self.assertEqual(header, "Hello")

if __name__ == "__main__":
    unittest.main()