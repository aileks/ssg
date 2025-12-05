import unittest

from markdown_to_html import markdown_to_html_node


class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraphs(self):
        md = "This is **bolded** paragraph\ntext in a p\ntag here\n\nThis is another paragraph with _italic_ text and `code` here\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = "```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = "# This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>This is a heading</h1></div>")

    def test_heading_with_inline(self):
        md = "## This is **bold** heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is <b>bold</b> heading</h2></div>",
        )

    def test_quote(self):
        md = "> This is a quote\n> with multiple lines"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote\nwith multiple lines</blockquote></div>",
        )

    def test_quote_with_inline(self):
        md = "> This is a **bold** quote\n> with _italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a <b>bold</b> quote\nwith <i>italic</i> text</blockquote></div>",
        )

    def test_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )

    def test_unordered_list_with_inline(self):
        md = "- Item with **bold**\n- Item with _italic_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item with <b>bold</b></li><li>Item with <i>italic</i></li></ul></div>",
        )

    def test_ordered_list(self):
        md = "1. First\n2. Second\n3. Third"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>",
        )

    def test_ordered_list_with_inline(self):
        md = "1. Item with `code`\n2. Item with **bold**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Item with <code>code</code></li><li>Item with <b>bold</b></li></ol></div>",
        )

    def test_mixed_blocks(self):
        md = "# Heading\n\nThis is a paragraph with **bold** text.\n\n- List item 1\n- List item 2\n\n> A quote here\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1><p>This is a paragraph with <b>bold</b> text.</p><ul><li>List item 1</li><li>List item 2</li></ul><blockquote>A quote here</blockquote></div>",
        )

    def test_complex_document(self):
        md = '# My Blog Post\n\nThis is an intro paragraph with **bold** and _italic_ text.\n\n## Section 1\n\n- Point 1\n- Point 2\n- Point 3\n\n## Code Example\n\n```\ndef hello():\n    print("world")\n```\n\n> Always remember to **have fun**!\n\n1. First step\n2. Second step\n'
        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertIn("<h1>My Blog Post</h1>", html)
        self.assertIn("<h2>Section 1</h2>", html)
        self.assertIn("<ul><li>Point 1</li>", html)
        self.assertIn("<pre><code>", html)
        self.assertIn("<blockquote>Always remember to <b>have fun</b>!", html)
        self.assertIn("<ol><li>First step</li>", html)


if __name__ == "__main__":
    unittest.main()
