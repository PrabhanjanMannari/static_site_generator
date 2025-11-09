import unittest 

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_wrong_args(self):
        self.assertRaises(ValueError, LeafNode, None, "value", {"children" : [HTMLNode(), HTMLNode()]})

    def test_to_html(self):
        tag: str              = "p"
        value: str            = "This is a value"
        prop_key: str         = "href"
        prop_val: str         = "https://www.google.com"
        props: Dict[str, str] = {prop_key : prop_val}

        tagged_output: str = f"<{tag}>{value}</{tag}>"
        props_output: str  = f'<{tag} {prop_key}="{prop_val}">{value}</{tag}>'


        leaf_node: LeafNode = LeafNode(tag = None, value = value)
        self.assertEqual(leaf_node.to_html(), value)

        leaf_node: LeafNode = LeafNode(tag = tag, value = value)
        self.assertEqual(leaf_node.to_html(), tagged_output)

        leaf_node: LeafNode = LeafNode(tag = tag, value = value, props = props)
        self.assertEqual(leaf_node.to_html(), props_output)

if __name__ == "__main__":
    unittest.main()

