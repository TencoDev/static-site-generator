import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()