import unittest 

from conversions import *

class TestConversions(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_italic_code(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

        node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")

        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.link.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")

        self.assertIsNotNone(html_node.props)
        self.assertIsInstance(html_node.props, dict)
        doesContainKey = "href" in html_node.props
        self.assertEqual(doesContainKey, True)
        prop_val = html_node.props["href"]
        self.assertEqual(prop_val, "www.link.com")

    def test_img(self):
        node = TextNode("Image not found", TextType.IMAGE, "www.link.com/img")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

        self.assertIsNotNone(html_node.props)
        self.assertIsInstance(html_node.props, dict)

        doesContainKey = "src" in html_node.props
        self.assertEqual(doesContainKey, True)
        prop_val = html_node.props["src"]
        self.assertEqual(prop_val, "www.link.com/img")

        doesContainKey = "alt" in html_node.props
        self.assertEqual(doesContainKey, True)
        prop_val = html_node.props["alt"]
        self.assertEqual(prop_val, "Image not found")



if __name__ == "__main__":
    unittest.main()
