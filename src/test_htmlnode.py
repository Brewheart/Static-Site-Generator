import unittest

from htmlnode import HTMLNode

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

    def test_to_html(self):
        node = HTMLNode(tag="a", value="click me")
        with self.assertRaises(NotImplementedError):
            node.to_html()