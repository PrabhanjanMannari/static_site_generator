import unittest 
from conversions import * 

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        md = """
This is some code `int main() { return 0;}`
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is some code `int main() { return 0;}`"])

    def test_multiple_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_empty_blocks(self):
        md = """



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

        md = """
This is **bolded** paragraph





This is some code `int main() { return 0;}`
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is **bolded** paragraph",  "This is some code `int main() { return 0;}`"])

if __name__ == "__main__":
    unittest.main()
