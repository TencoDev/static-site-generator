import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text_type_eq(self):
        node = TextNode("This is node 1's text", TextType.ITALIC)
        node2 = TextNode("This is node 2's text", TextType.ITALIC)
        self.assertEqual(node.text_type, node2.text_type)
        
    def test_text_type_noteq(self):
        node = TextNode("This is node 1's text", TextType.BOLD)
        node2 = TextNode("This is node 2's text", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_is_url_none(self):
        node = TextNode("This is just text", TextType.TEXT)
        self.assertEqual(node.url, None )
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_text_invalid_type(self):
        node = TextNode("This is invalid text", "INVALID")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
    
    def test_text_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_text_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")
        
    def test_text_code(self):
        node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")
        
    def test_text_anchor(self):
        node = TextNode("This is anchor text", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is anchor text")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_text_img(self):
        node = TextNode("cat image", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "cat image" })
        

if __name__ == "__main__":
    unittest.main()