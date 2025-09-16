# python

import unittest
from textnode import TextNode, TextType
from converters import text_node_to_html_node
from converters import markdown_to_html_node


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

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
        > This is a quote
    > with some _italic_ and **bold**
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><blockquote>This is a quote with some <i>italic</i> and <b>bold</b></blockquote></div>"
                )


    def test_headingblock(self):
        md = """
    # Title with **bold**
    ### Sub _title_
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><h1>Title with <b>bold</b></h1><h3>Sub <i>title</i></h3></div>"
                )

    def test_unordered_list(self):
        md = """
    - First item with **bold**
    - Second item with _italic_
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>First item with <b>bold</b></li><li>Second item with <i>italic</i></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
    1. First with **bold**
    2. Second with _italic_
    3. Third with `code`
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First with <b>bold</b></li><li>Second with <i>italic</i></li><li>Third with <code>code</code></li></ol></div>",
        )
