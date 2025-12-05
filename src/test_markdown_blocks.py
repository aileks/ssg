import unittest

from markdown_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_single_block(self):
        md = "This is a single block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single block"])

    def test_markdown_to_blocks_multiple_blocks(self):
        md = "Block 1\n\nBlock 2\n\nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2", "Block 3"])

    def test_markdown_to_blocks_strips_whitespace(self):
        md = "  Block 1  \n\n  Block 2  "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2"])

    def test_markdown_to_blocks_multiple_newlines(self):
        md = "Block 1\n\n\n\nBlock 2"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2"])

    def test_markdown_to_blocks_leading_trailing_newlines(self):
        md = "\n\nBlock 1\n\nBlock 2\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2"])

    def test_markdown_to_blocks_preserves_internal_newlines(self):
        md = "Line 1\nLine 2\n\nBlock 2"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Line 1\nLine 2", "Block 2"])

    def test_markdown_to_blocks_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_only_whitespace(self):
        md = "   \n\n   \n\n   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_heading_and_paragraph(self):
        md = "# Heading\n\nThis is a paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["# Heading", "This is a paragraph"])

    def test_markdown_to_blocks_list(self):
        md = "- Item 1\n- Item 2\n- Item 3\n\nNext block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["- Item 1\n- Item 2\n- Item 3", "Next block"],
        )

    def test_markdown_to_blocks_code_block(self):
        md = "```\ncode here\n```\n\nNext block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["```\ncode here\n```", "Next block"],
        )

    def test_markdown_to_blocks_complex_document(self):
        md = "# My Document\n\nThis is the introduction paragraph.\n\n## Section 1\n\n- List item 1\n- List item 2\n\n## Section 2\n\nAnother paragraph with **bold** text.\n\n```\ndef hello():\n    print(\"world\")\n```\n\nFinal paragraph."
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# My Document",
                "This is the introduction paragraph.",
                "## Section 1",
                "- List item 1\n- List item 2",
                "## Section 2",
                "Another paragraph with **bold** text.",
                "```\ndef hello():\n    print(\"world\")\n```",
                "Final paragraph.",
            ],
        )


if __name__ == "__main__":
    unittest.main()
