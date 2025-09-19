import unittest

from textnode import TextNode, TextType
from converters import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_notEqual(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_texttype_is_different(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node.text_type, node2.text_type)
    
    def test_anchor(self):
        n = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        html = text_node_to_html_node(n).to_html()
        self.assertEqual(html, '<a href="https://www.boot.dev">Boot.dev</a>')


if __name__ == "__main__":
    unittest.main()

