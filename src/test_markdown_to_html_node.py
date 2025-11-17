import unittest 

from html_conversions import *

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_linear_case(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

        md = """```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></div>",
        )

        md = """# My Project

This is a paragraph explaining the purpose of the project.
It includes **bold text** and _italic text_.

## Features

1. Easy to use  
2. Fast  
3. Open-source

> 'Good software is built by good developers.'
"""

        expected = """<div><h>My Project</h><p>This is a paragraph explaining the purpose of the project.
It includes <b>bold text</b> and <i>italic text</i>.</p><h>Features</h><ol><li>Easy to use</li><li>Fast</li><li>Open-source</li></ol><q>'Good software is built by good developers.'</q></div>"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected)


    def test_nested_cases(self):
        md = """# **Bold Heading** with `code`

1. _Italic item_
2. ![Sample Image](https://via.placeholder.com/150)
3. [link](https://example.com)"""

        expected = """<div><h><b>Bold Heading</b> with <code>code</code></h><ol><li><i>Italic item</i></li><li><img src="https://via.placeholder.com/150" alt="Sample Image"></li><li><a href="https://example.com">link</a></li></ol></div>"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected)

if __name__ == "__main__":
    unittest.main()
