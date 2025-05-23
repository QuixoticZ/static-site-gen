import unittest

from htmlnode import *
from textnode import TextNode,TextType

class TestHMTLNode(unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode("p","link",props={"href":"https://www.google.com","target":"_blank"})
        self.assertEqual(node1.__repr__(),"HTMLNode(p, link, None, {'href': 'https://www.google.com', 'target': '_blank'})")

    def test_no_prop_to_html(self):
        node1 = HTMLNode("p","link")
        self.assertEqual(node1.props_to_html(),"")

    def test_single_prop_to_html(self):
        node1 = HTMLNode("p","link",props={"href":"https://www.google.com"})
        self.assertEqual(node1.props_to_html(),' href="https://www.google.com"')

    def test_multiple_prop_to_html(self):
        node1 = HTMLNode("p","link",props={"href":"https://www.google.com","target":"_blank"})
        self.assertEqual(node1.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_empty_prop(self):
        node1 = HTMLNode("p","link",props={"href":"","target":"_blank"})
        self.assertEqual(node1.props_to_html(),' href="" target="_blank"')
     
    def test_only_tag(self):
        node1 = HTMLNode("p")
        self.assertEqual(node1.__repr__(),"HTMLNode(p, None, None, None)")

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )    
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_no_value(self):
        with self.assertRaises(TypeError):
            node = LeafNode("p",props={"href": "https://www.google.com"})

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )



if __name__ == "__main__":
    unittest.main()