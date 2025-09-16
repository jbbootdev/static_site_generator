import unittest
from block_type import BlockType
from utils import block_to_block


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_levels(self):
        self.assertEqual(block_to_block("# Title"), BlockType.HEADING)
        self.assertEqual(block_to_block("###### Tiny"), BlockType.HEADING)

    def test_heading_needs_space(self):
        self.assertEqual(block_to_block("####NoSpace"), BlockType.PARAGRAPH)

    def test_code_fence_basic(self):
        block = "```\nprint('hi')\n```"
        self.assertEqual(block_to_block(block), BlockType.CODE)

    def test_code_with_language_label(self):
        block = "```python\nx=1\n```"
        self.assertEqual(block_to_block(block), BlockType.CODE)

    def test_quote_all_lines_prefixed(self):
        block = "> a\n> b\n> c"
        self.assertEqual(block_to_block(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- item 1\n- item 2"
        self.assertEqual(block_to_block(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_requires_space(self):
        self.assertEqual(block_to_block("-item"), BlockType.PARAGRAPH)

    def test_ordered_list_strict_increment(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(block_to_block(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_start(self):
        block = "2. starts wrong\n3. nope"
        self.assertEqual(block_to_block(block), BlockType.PARAGRAPH)

    def test_ordered_list_gap_breaks(self):
        block = "1. ok\n3. skipped"
        self.assertEqual(block_to_block(block), BlockType.PARAGRAPH)

    def test_paragraph_fallback(self):
        self.assertEqual(block_to_block("Just some text."), BlockType.PARAGRAPH)

    def test_empty_is_paragraph(self):
        self.assertEqual(block_to_block(""), BlockType.PARAGRAPH)
