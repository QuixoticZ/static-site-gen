import unittest

from htmlnode import HTMLNode

class TestHMTLNode(unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode("p","link",props={"href":"https://www.google.com","target":"_blank"})
        print(node1.__repr__)

    def test_no_prop_to_html(self):
        node1 = HTMLNode("p","link")
        print(node1.props_to_html())

    def test_single_prop_to_html(self):
        node1 = HTMLNode("p","link",props={"href":"https://www.google.com"})
        self.assertEqual(node1.props_to_html()," href: https://www.google.com")

    def test_multiple_prop_to_html(self):
        node1 = HTMLNode("p","link",props={"href":"https://www.google.com","target":"_blank"})
        self.assertEqual(node1.props_to_html(),' href: "https://www.google.com" target: "_blank"')

    def test_empty_prop(self):
        node1 = HTMLNode("p","link",props={"href":"","target":"_blank"})
        self.assertEqual(node1.props_to_html(),' href: "" target: "_blank"')
     
    def test_only_tag(self):
        node1 = HTMLNode("p")
        self.assertEqual(node1.__repr__,"HMTLNode(p,None,None,None)")

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