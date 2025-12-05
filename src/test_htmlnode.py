import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_single_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        result = node.props_to_html()
        self.assertIn('href="https://www.google.com"', result)
        self.assertIn('target="_blank"', result)
        self.assertTrue(result.startswith(" "))

    def test_props_to_html_with_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_empty_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_htmlnode_constructor_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_htmlnode_constructor_with_values(self):
        node = HTMLNode(
            tag="p", value="This is a paragraph", children=[], props={"class": "text"}
        )
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    def test_to_html_raises_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Bold text")
        self.assertEqual(node.to_html(), "<b>Bold text</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Italic text")
        self.assertEqual(node.to_html(), "<i>Italic text</i>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", "print('hello')")
        self.assertEqual(node.to_html(), "<code>print('hello')</code>")

    def test_leaf_to_html_no_value_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_img_with_props(self):
        node = LeafNode("img", "", {"src": "image.png", "alt": "An image"})
        result = node.to_html()
        self.assertIn('src="image.png"', result)
        self.assertIn('alt="An image"', result)


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            child_node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_no_tag_raises_error(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children_raises_error(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_nested_parents(self):
        grandchild = LeafNode("span", "text")
        child = ParentNode("div", [grandchild])
        parent = ParentNode("section", [child])
        self.assertEqual(
            parent.to_html(),
            "<section><div><span>text</span></div></section>",
        )

    def test_to_html_with_mixed_children(self):
        child1 = LeafNode("b", "Bold")
        child2 = ParentNode("span", [LeafNode(None, "nested")])
        child3 = LeafNode("i", "Italic")
        parent = ParentNode("p", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold</b><span>nested</span><i>Italic</i></p>",
        )

    def test_to_html_with_empty_children_list(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "article",
                            [LeafNode("p", "Hello")],
                        )
                    ],
                )
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<div><section><article><p>Hello</p></article></section></div>",
        )


if __name__ == "__main__":
    unittest.main()
