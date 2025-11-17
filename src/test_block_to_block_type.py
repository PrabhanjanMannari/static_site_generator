import unittest 
from conversions import * 

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        text: str = "# HEADING 1"
        self.assertEqual(BlockType.HEADING, block_to_block_type(text))

        text = "## HEADING 2"
        self.assertEqual(BlockType.HEADING, block_to_block_type(text))

        text = "### HEADING 3"
        self.assertEqual(BlockType.HEADING, block_to_block_type(text))

        text = "#### HEADING 4"
        self.assertEqual(BlockType.HEADING, block_to_block_type(text))

        text = "##### HEADING 5"
        self.assertEqual(BlockType.HEADING, block_to_block_type(text))

        text = "###### HEADING 6"
        self.assertEqual(BlockType.HEADING, block_to_block_type(text))

        text = "## HEADING WITH MULTIPLE LINES\nTHIS IS LINE 2"
        self.assertEqual(BlockType.HEADING, block_to_block_type(text))

    def test_code(self):
        text: str = "```CODE```"
        self.assertEqual(BlockType.CODE, block_to_block_type(text))

        text = "```CODE\nWITH\nMULTIPLE\nLINES```"
        self.assertEqual(BlockType.CODE, block_to_block_type(text))

        text = "```CODE WITH `BACKTICKS` AGAIN```"
        self.assertEqual(BlockType.CODE, block_to_block_type(text))

    def test_quote(self):
        text: str = "> This is a quote with a space in front"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(text))

        text = """>This is a quote 
>This is another quote"""
        self.assertEqual(BlockType.QUOTE, block_to_block_type(text))

        text = """>This is a quote
>This is another quote
>This is yet another quote"""
        self.assertEqual(BlockType.QUOTE, block_to_block_type(text))

    def test_unordered_list(self):
        text: str = "- UL with single item"
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(text))

        text = """- UL item 1
- UL item 2
- UL item 3"""
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(text))

    def test_ordered_list(self):
        text: str = "1. OL with single item"
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(text))

        text = """1. OL item 1
2. OL item 2
3. OL item 3"""

    def test_paragraph(self):
        text: str = "###NOT HEADING"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = "########### NOT HEADING "
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = "```NOT CODE``"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = "``NOT CODE``"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = "` NOT CODE`"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = """>This is a quote 
<This is not a quote"""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = """>This is a quote 
- This is list item"""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = """- UL item 1
2. OL item 2
- UL item 3"""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

        text = """1. OL item 1
3. OL item 3
3. OL item 3"""
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(text))

if __name__ == "__main__":
    unittest.main()
