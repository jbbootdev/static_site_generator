# python

import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        test_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        htmlNode = HTMLNode("<p>", "Test", "", test_props)
        self.assertEqual(
            htmlNode.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )
