import unittest

from extract_markdown import (
    extract_markdown_images,
    extract_markdown_links,
)


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_images_no_images(self):
        text = "This is text with no images"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_images_alt_text_with_spaces(self):
        text = "This is ![a very long alt text](https://example.com/image.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [("a very long alt text", "https://example.com/image.png")],
            matches,
        )

    def test_extract_markdown_images_complex_url(self):
        text = "Check ![screenshot](https://example.com/path/to/image.jpg?size=large&format=png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                (
                    "screenshot",
                    "https://example.com/path/to/image.jpg?size=large&format=png",
                )
            ],
            matches,
        )


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multiple(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_links_no_links(self):
        text = "This is text with no links"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links_with_anchor_text_spaces(self):
        text = "Click [here for more info](https://example.com/page)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("here for more info", "https://example.com/page")],
            matches,
        )

    def test_extract_markdown_links_complex_url(self):
        text = "Visit [my site](https://example.com/path?query=value&other=123#section)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                (
                    "my site",
                    "https://example.com/path?query=value&other=123#section",
                )
            ],
            matches,
        )

    def test_extract_markdown_links_not_images(self):
        text = "This is ![not a link](https://example.com/image.png) and [a link](https://example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("a link", "https://example.com")], matches)

    def test_extract_markdown_links_mixed_with_images(self):
        text = "Image: ![alt](https://example.com/img.png) and link: [text](https://example.com)"
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertListEqual([("alt", "https://example.com/img.png")], image_matches)
        self.assertListEqual([("text", "https://example.com")], link_matches)

    def test_extract_markdown_links_single_word(self):
        text = "Check [here](https://boot.dev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("here", "https://boot.dev")], matches)


if __name__ == "__main__":
    unittest.main()
