import unittest 

from conversions import * 

class TestTextToTextNodes(unittest.TestCase):
    
    def test_vanilla_cases(self):
        text: str = "This is a **bold sentence** with a simple [link](https://example.com) and an inline `code` snippet. Here is an image: ![Alt text](https://placekitten.com/200/200)"
        node_list: list[TextNode] = text_to_textnodes(text)
        self.assertEqual(len(node_list), 8)
        self.assertEqual(node_list[0], TextNode("This is a "))
        self.assertEqual(node_list[1], TextNode("bold sentence", TextType.BOLD))
        self.assertEqual(node_list[2], TextNode(" with a simple "))
        self.assertEqual(node_list[3], TextNode("link", TextType.LINK, "https://example.com"))
        self.assertEqual(node_list[4], TextNode(" and an inline "))
        self.assertEqual(node_list[5], TextNode("code", TextType.CODE))
        self.assertEqual(node_list[6], TextNode(" snippet. Here is an image: "))
        self.assertEqual(node_list[7], TextNode("Alt text", TextType.IMAGE, "https://placekitten.com/200/200"))

        text = "You can _italicize text_ and also write `print('hello')` as code. For more details, visit [Python Docs](https://docs.python.org). Here's a sample image: ![Image](https://picsum.photos/200)"
        node_list = text_to_textnodes(text)
        self.assertEqual(len(node_list), 8)
        self.assertEqual(node_list[0], TextNode("You can "))
        self.assertEqual(node_list[1], TextNode("italicize text", TextType.ITALIC))
        self.assertEqual(node_list[2], TextNode(" and also write "))
        self.assertEqual(node_list[3], TextNode("print('hello')", TextType.CODE))
        self.assertEqual(node_list[4], TextNode(" as code. For more details, visit "))
        self.assertEqual(node_list[5], TextNode("Python Docs", TextType.LINK, "https://docs.python.org"))
        self.assertEqual(node_list[6], TextNode(". Here's a sample image: "))
        self.assertEqual(node_list[7], TextNode("Image", TextType.IMAGE, "https://picsum.photos/200"))

        text = "This line has **bold text**, _italic text_, and a `variable name`. Check out [this site](https://github.com). Image here: ![Random](https://picsum.photos/300)"
        node_list = text_to_textnodes(text)
        self.assertEqual(len(node_list), 10)
        self.assertEqual(node_list[0], TextNode("This line has "))
        self.assertEqual(node_list[1], TextNode("bold text", TextType.BOLD))
        self.assertEqual(node_list[2], TextNode(", "))
        self.assertEqual(node_list[3], TextNode("italic text", TextType.ITALIC))
        self.assertEqual(node_list[4], TextNode(", and a "))
        self.assertEqual(node_list[5], TextNode("variable name", TextType.CODE))
        self.assertEqual(node_list[6], TextNode(". Check out "))
        self.assertEqual(node_list[7], TextNode("this site", TextType.LINK, "https://github.com"))
        self.assertEqual(node_list[8], TextNode(". Image here: "))
        self.assertEqual(node_list[9], TextNode("Random", TextType.IMAGE, "https://picsum.photos/300"))

    def test_corner_cases(self):
        text: str = "**BoldText** ends here. Visit [Example](https://example.com). Another sentence ends with a link: [Docs](https://docs.python.org)."
        node_list: list[TextNode] = text_to_textnodes(text)
        self.assertEqual(len(node_list), 6)
        self.assertEqual(node_list[0], TextNode("BoldText", TextType.BOLD))
        self.assertEqual(node_list[1], TextNode(" ends here. Visit "))
        self.assertEqual(node_list[2], TextNode("Example", TextType.LINK, "https://example.com"))
        self.assertEqual(node_list[3], TextNode(". Another sentence ends with a link: "))
        self.assertEqual(node_list[4], TextNode("Docs", TextType.LINK, "https://docs.python.org"))
        self.assertEqual(node_list[5], TextNode("."))

        text = "![StartImage](https://placekitten.com/150/150) This line mixes an image at the start, followed by _italic text_ and **bold words** before finishing with `final token`."
        node_list = text_to_textnodes(text)
        self.assertEqual(len(node_list), 8)
        self.assertEqual(node_list[0], TextNode("StartImage", TextType.IMAGE, "https://placekitten.com/150/150"))
        self.assertEqual(node_list[1], TextNode(" This line mixes an image at the start, followed by "))
        self.assertEqual(node_list[2], TextNode("italic text", TextType.ITALIC))
        self.assertEqual(node_list[3], TextNode(" and "))
        self.assertEqual(node_list[4], TextNode("bold words", TextType.BOLD))
        self.assertEqual(node_list[5], TextNode(" before finishing with "))
        self.assertEqual(node_list[6], TextNode("final token", TextType.CODE))
        self.assertEqual(node_list[7], TextNode("."))

        text = "_Italic text_ then a [middle link](https://example.com) then **bold text** followed by an image: ![Alt](https://picsum.photos/150)"
        node_list = text_to_textnodes(text)
        self.assertEqual(len(node_list), 7)
        self.assertEqual(node_list[0], TextNode("Italic text", TextType.ITALIC))
        self.assertEqual(node_list[1], TextNode(" then a "))
        self.assertEqual(node_list[2], TextNode("middle link", TextType.LINK, "https://example.com"))
        self.assertEqual(node_list[3], TextNode(" then "))
        self.assertEqual(node_list[4], TextNode("bold text", TextType.BOLD))
        self.assertEqual(node_list[5], TextNode(" followed by an image: "))
        self.assertEqual(node_list[6], TextNode("Alt", TextType.IMAGE, "https://picsum.photos/150"))

if __name__ == "__main__":
    unittest.main()
