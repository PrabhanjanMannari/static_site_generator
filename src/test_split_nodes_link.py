import unittest 

from conversions import *

class TestSplitNodesLink(unittest.TestCase):

    def test_one_link(self):
        node: TextNode = TextNode(
                "Here's a cute cat: [Cat](https://placekitten.com/200/200)",
                )
        new_nodes: list[TextNode] = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("Here's a cute cat: "))
        self.assertEqual(new_nodes[1], TextNode("Cat", TextType.LINK, "https://placekitten.com/200/200"))

    def test_two_links(self):
        node: TextNode = TextNode(
                "Here's a cute cat and dog: [Cat](https://placekitten.com/200/200), [Dog](https://placedog.net/200/200)"
                )
        new_nodes: list[TextNode] = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0], TextNode("Here's a cute cat and dog: "))
        self.assertEqual(new_nodes[1], TextNode("Cat", TextType.LINK, "https://placekitten.com/200/200"))
        self.assertEqual(new_nodes[2], TextNode(", "))
        self.assertEqual(new_nodes[3], TextNode("Dog", TextType.LINK, "https://placedog.net/200/200"))

    def test_only_link(self):
        node: TextNode = TextNode(
                "[Cat](https://placekitten.com/200/200)"
                )

        new_nodes: list[TextNode] = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("Cat", TextType.LINK, "https://placekitten.com/200/200"))

    def test_two_link_no_space(self):
        node: TextNode = TextNode(
                "[Cat](https://placekitten.com/200/200)[Dog](https://placedog.net/200/200)"
                )
        new_nodes: list[TextNode] = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("Cat", TextType.LINK, "https://placekitten.com/200/200"))
        self.assertEqual(new_nodes[1], TextNode("Dog", TextType.LINK, "https://placedog.net/200/200"))

    def test_multiple_nodes(self):
        node1: TextNode = TextNode(
                "Here's a cute cat and dog: [Cat](https://placekitten.com/200/200), [Dog](https://placedog.net/200/200)"
                )
        node2: TextNode = TextNode(
                "Here's a cute cat and dog: [Cat](https://placekitten.com/200/200), [Dog](https://placedog.net/200/200)"
                )
        new_nodes = split_nodes_link([node1, node2])
        self.assertEqual(len(new_nodes), 8)
        self.assertEqual(new_nodes[0], TextNode("Here's a cute cat and dog: "))
        self.assertEqual(new_nodes[1], TextNode("Cat", TextType.LINK, "https://placekitten.com/200/200"))
        self.assertEqual(new_nodes[2], TextNode(", "))
        self.assertEqual(new_nodes[3], TextNode("Dog", TextType.LINK, "https://placedog.net/200/200"))
        self.assertEqual(new_nodes[4], TextNode("Here's a cute cat and dog: "))
        self.assertEqual(new_nodes[5], TextNode("Cat", TextType.LINK, "https://placekitten.com/200/200"))
        self.assertEqual(new_nodes[6], TextNode(", "))
        self.assertEqual(new_nodes[7], TextNode("Dog", TextType.LINK, "https://placedog.net/200/200"))


if __name__ == "__main__":
    unittest.main()
