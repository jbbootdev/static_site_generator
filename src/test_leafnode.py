# python

import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_p(self):
        leafNode = LeafNode("p", "This is a paragraph of text.")
        self.assertIn(leafNode.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_with_div(self):
        leafNode = LeafNode("div", "This is a paragraph of text.")
        self.assertIn(leafNode.to_html(), "<div>This is a paragraph of text.</div>")
