from conversions import *
import unittest 

class TestSplitDelimiter(unittest.TestCase):
    def test_exception(self):
        node: TextNode = TextNode("Wrong text 'this is code")
        self.assertRaises(TypeError, split_nodes_delimiter([node], "`", TextType.CODE))

    def test_bold(self):
        node: TextNode = TextNode("This is text with a **bold text** word", TextType.TEXT)

        new_nodes: list[TextNode]      = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes: list[TextNode] = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        for node1, node2 in zip(new_nodes, expected_nodes):
            self.assertEqual(node1, node2)


    def test_italic(self):
        node: TextNode = TextNode("This is text with a _italic text_ word", TextType.TEXT)

        new_nodes: list[TextNode]      = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes: list[TextNode] = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        for node1, node2 in zip(new_nodes, expected_nodes):
            self.assertEqual(node1, node2)

    def test_code(self):
        node: TextNode = TextNode("This is text with a `code` word", TextType.TEXT)

        new_nodes: list[TextNode]      = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes: list[TextNode] = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        for node1, node2 in zip(new_nodes, expected_nodes):
            self.assertEqual(node1, node2)


    def test_bold_italic(self):
        node: TextNode = TextNode("This is text with a **bold text** and _italic text_", TextType.TEXT)

        new_nodes: list[TextNode]      = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes: list[TextNode] = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" and _italic text_", TextType.TEXT),
        ]
        for node1, node2 in zip(new_nodes, expected_nodes):
            self.assertEqual(node1, node2)

    def test_bold_code(self):
        node: TextNode = TextNode("This is text with a **bold text** and `code`", TextType.TEXT)

        new_nodes: list[TextNode]      = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes: list[TextNode] = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" and `code`", TextType.TEXT),
        ]
        for node1, node2 in zip(new_nodes, expected_nodes):
            self.assertEqual(node1, node2)

    def test_italic_code(self):
        node: TextNode = TextNode("This is text with a _italic text_ and `code`", TextType.TEXT)

        new_nodes: list[TextNode]      = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes: list[TextNode] = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" and `code`", TextType.TEXT),
        ]
        for node1, node2 in zip(new_nodes, expected_nodes):
            self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
