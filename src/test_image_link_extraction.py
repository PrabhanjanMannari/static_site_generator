import unittest

from conversions import * 

class TestImageLinkExtraction(unittest.TestCase):
    def test_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_link(self):
        matches = extract_markdown_links(
            "This is text with an [clickable](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("clickable", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_image_with_link(self):
        matches = extract_markdown_images(
            "This is text with an [clickable](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_link_with_image(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()


