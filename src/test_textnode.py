import unittest 

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_url_none(self):
        node1 = TextNode("This is a test", TextType.TEXT)
        self.assertEqual(node1.url, None)

    def test_text_not_equal(self):
        node1 = TextNode("This is some text", TextType.TEXT)
        node2 = TextNode("This is some other text", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_type_not_equal(self):
        node1 = TextNode("This is some text", TextType.TEXT)
        node2 = TextNode("This is some text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
