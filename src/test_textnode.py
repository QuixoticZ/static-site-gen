import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node,node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.LINK,"https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertNotEqual(node,node2)

    def test_declared_none(self):
        node = TextNode("This is a text node", TextType.ITALIC, None)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node,node2)

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