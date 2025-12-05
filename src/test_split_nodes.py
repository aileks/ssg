import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_split(self):
        node = TextNode(
            "This is text with a `code block` word",
            TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_bold_split(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_italic_split(self):
        node = TextNode("This is _italic_ text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_non_text_node_passes_through(self):
        node = TextNode("bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_multiple_nodes(self):
        nodes = [
            TextNode("This is **bold** text", TextType.TEXT),
            TextNode("This is normal text", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
                TextNode("This is normal text", TextType.TEXT),
            ],
        )

    def test_mixed_node_types(self):
        nodes = [
            TextNode("This is **bold**", TextType.TEXT),
            TextNode("already bold", TextType.BOLD),
        ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode("already bold", TextType.BOLD),
            ],
        )

    def test_multiple_delimiters(self):
        node = TextNode(
            "This is `code` and more `code` here",
            TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and more ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" here", TextType.TEXT),
            ],
        )

    def test_delimiter_at_start(self):
        node = TextNode("`code` at start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("code", TextType.CODE),
                TextNode(" at start", TextType.TEXT),
            ],
        )

    def test_delimiter_at_end(self):
        node = TextNode("at end `code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("at end ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
        )

    def test_no_delimiter_present(self):
        node = TextNode("This is plain text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [node])

    def test_unclosed_delimiter_raises_error(self):
        node = TextNode("This is `unclosed code", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_only_delimiter(self):
        node = TextNode("`code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [TextNode("code", TextType.CODE)],
        )


if __name__ == "__main__":
    unittest.main()
