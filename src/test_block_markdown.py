import unittest
from block_markdown import *

class TestTextNode(unittest.TestCase):
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

    def assertEqual(self,input1,input2):
        if input1.__eq__(input2) == True:
            return True
        else:
            return False
        
    def assertNotEqual(self,input1,input2):
        if input1.__eq__(input2) == True:
            return False
        else:
            return True

if __name__ == "__main__":
    unittest.main()