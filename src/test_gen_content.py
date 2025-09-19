from gen_content import extract_title
import unittest

class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        md = "# Tolkien Fan Club"
        extracted_title = extract_title(md)
        self.assertEqual(extracted_title, "Tolkien Fan Club")

    def test_extract_title_raises_when_no_h1(self):
        md = "## Not a top header\nSome text"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_finds_first_h1(self):
        md = "## Sub\n# Main Title\nMore"
        result = extract_title(md)
        self.assertEqual(result, "Main Title")
