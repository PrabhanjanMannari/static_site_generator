import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_default_init(self):
        html_node: HTMLNode = HTMLNode()

        self.assertIsNone(html_node.tag)
        self.assertIsNone(html_node.value)
        self.assertIsNone(html_node.children)
        self.assertIsNone(html_node.props)

    def test_value_init(self):
        html_node: HTMLNode = HTMLNode(tag = "<p>", 
                                       value = "Lorem ipsum dolor sit amet", 
                                       children = [HTMLNode()], 
                                       props = {"key" : "value"})

        self.assertEqual(html_node.tag, "<p>")
        self.assertEqual(html_node.value, "Lorem ipsum dolor sit amet")
        self.assertIsInstance(html_node.children, list)
        self.assertIsNotNone(html_node.children)
        for child in html_node.children:
            self.assertIsInstance(child, HTMLNode)
        self.assertIsNotNone(html_node.props)
        for key, value in html_node.props.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, str)

            self.assertEqual(key, "key")
            self.assertEqual(value, "value")

    def test_props_to_html(self):
        html_node: HTMLNode = HTMLNode(props = {"href"   : "https://www.google.com", 
                                                "target" : "blank"}
                              )
        self.assertEqual(html_node.props_to_html(), ' href="https://www.google.com" target="blank"')


if __name__ == "__main__":
    unittest.main()
