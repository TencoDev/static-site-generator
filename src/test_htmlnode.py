import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        
    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "Paragraph 1")
        child2 = LeafNode("p", "Paragraph 2")
        parent_node = ParentNode("div", [child1, child2])
        
        self.assertEqual(
            parent_node.to_html(),
            "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"
        )
        
    def test_to_html_with_multiple_children(self):
        grandchild_node = LeafNode("b", "grandchild")
        child1 = ParentNode("div", [grandchild_node])
        child2 = LeafNode("p", "Paragraph")
        parent_node = ParentNode("div", [child1, child2])
        
        self.assertEqual(
            parent_node.to_html(),
            "<div><div><b>grandchild</b></div><p>Paragraph</p></div>"
        )
        
    



if __name__ == "__main__":
    unittest.main()