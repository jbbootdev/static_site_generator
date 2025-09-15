# python

import unittest
from textnode import TextNode, TextType
from converters import text_node_to_html_node


class TestConverters(unittest.TestCase):
    def test_converting_texttype_text_to_html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "This is a text node")

    def test_converting_texttype_bold_to_html_node(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual("b", html_node.tag)
        self.assertEqual(html_node.value, "This is a bold node")

    def test_converting_texttype_italic_to_html_node(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual("i", html_node.tag)
        self.assertEqual(html_node.value, "This is a italic node")

    def test_converting_texttype_code_to_html_node(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual("code", html_node.tag)
        self.assertEqual(html_node.value, "This is a code node")

    def test_converting_texttype_link_to_html_node(self):
        node = TextNode("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual("a", html_node.tag)
        self.assertEqual(html_node.value, "This is a link node")

    def test_converting_texttype_image_to_html_node(self):
        node = TextNode("This is an image node", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual("img", html_node.tag)
        self.assertEqual(html_node.value, "This is an image node")
