import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode("p", "welcome to our website", None, {"href": "https://www.google.com", "target": "_blank",})
        props_string = html_node.props_to_html()
        ideal_string =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(props_string, ideal_string)
        
    def test_values(self):
        node = HTMLNode("div", "Container")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Container")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
        
    def test_repr(self):
        node = HTMLNode("p","What a strange world",None,{"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')



if __name__ == "__main__":
    unittest.main()