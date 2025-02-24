import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://test.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://test.com" target="_blank"')


    def test_node_to_string(self):
        node = HTMLNode (
            tag = "a",
            value = "click me",
            children = None,
            props = {"href": "https://test.com"}
        )
        expected = 'HTMLNode(tag="a", value="click me", children=None, props={\'href\': \'https://test.com\'})'
        self.assertEqual(repr(node), expected)

    def test_to_html_html(self):
        node = HTMLNode(tag="a", value="click me")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_to_html_leaf_string(self):
        node = LeafNode(tag="a", value="click me!", props={"href": "https://testing.com"})
        expected = '<a href="https://testing.com">click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_leaf_no_value(self):
        node = LeafNode(tag="a", value=None, props={"href": "https://testing.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_leaf_no_prop(self):
        node = LeafNode(tag="a", value="click me!", props=None)
        expected = "<a>click me!</a>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_parent_string(self):
        node = ParentNode(tag="p", children=[LeafNode("b", "bold text"), LeafNode("i", "italic text")])
        expected = "<p><b>bold text</b><i>italic text</i></p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_parent_no_tag(self):
        node = ParentNode(tag=None, children=[LeafNode("b", "bold text"), LeafNode("i", "italic text")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_parent_no_children(self):
        node = ParentNode(tag="a", children=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_parent_nested_parent(self):
        node = ParentNode(tag="a", children=[ParentNode(tag="p", children=[LeafNode("b", "bold text"), LeafNode("i", "italic text")])])
        expected = "<a><p><b>bold text</b><i>italic text</i></p></a>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_parent_nested_parent_and_leaf(self):
        node = ParentNode(tag="a", children=[ParentNode(tag="p", children=[LeafNode("b", "bold text"), LeafNode("i", "italic text")]), LeafNode("div", "divided")])
        expected = "<a><p><b>bold text</b><i>italic text</i></p><div>divided</div></a>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_parent_deep_nesting(self):
        node = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="section",
                    children=[
                        ParentNode(
                            tag="article",
                            children=[
                                LeafNode("b", "bold text"),
                                LeafNode("i", "italic text")
                            ]
                        ),
                        LeafNode("p", "paragraph")
                    ]
                ),
                LeafNode("span", "outer text")
            ]
        )
        expected = "<div><section><article><b>bold text</b><i>italic text</i></article><p>paragraph</p></section><span>outer text</span></div>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_parent_empty_children(self):
        node = ParentNode(tag="a", children=[])
        expected = "<a></a>"
        self.assertEqual(node.to_html(), expected)