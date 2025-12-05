import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_extract_title_with_content(self):
        md = "# Hello\n\nThis is content"
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_extract_title_with_leading_whitespace(self):
        md = "#   Hello World   "
        title = extract_title(md)
        self.assertEqual(title, "Hello World")

    def test_extract_title_multiple_lines_before(self):
        md = "Some intro\n\n# My Title\n\nContent here"
        title = extract_title(md)
        self.assertEqual(title, "My Title")

    def test_extract_title_no_h1_raises_error(self):
        md = "## Not an h1\n\nJust content"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_empty_raises_error(self):
        md = ""
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_only_hash_no_space_raises_error(self):
        md = "#NoSpace"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_with_special_characters(self):
        md = "# My Title: With Special Characters & Symbols!"
        title = extract_title(md)
        self.assertEqual(title, "My Title: With Special Characters & Symbols!")


if __name__ == "__main__":
    unittest.main()
