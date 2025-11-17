from typing import Callable 

from htmlnode import *
from textnode import *

from conversions import * 

def markdown_to_html_node(markdown: str)-> ParentNode: 
    blocks: list[str] = markdown_to_blocks(markdown)
    nested_nodes: list[HTMLNode] = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        if (block_type == BlockType.CODE):
            text_node: TextNode = TextNode(block[3:-3].lstrip("\n"), text_type = TextType.CODE)
            parent_node: ParentNode = text_node_to_html_node(text_node)
            nested_nodes.append(parent_node)
            continue

        children: list[HTMLNode] = text_to_children(block, block_type)
        match(block_type):
            case(BlockType.HEADING):
                parent_node: ParentNode = ParentNode(tag = "h", children = children)
            case(BlockType.QUOTE):
                parent_node: ParentNode = ParentNode(tag = "q", children = children)
            case(BlockType.UNORDERED_LIST):
                parent_node: ParentNode = ParentNode(tag = "ul", children = children)
            case(BlockType.ORDERED_LIST):
                parent_node: ParentNode = ParentNode(tag = "ol", children = children)
            case(BlockType.PARAGRAPH):
                parent_node: ParentNode = ParentNode(tag = "p", children = children)
            case _:
                raise TypeError("The block_type does not match any known BlockTypes")
        nested_nodes.append(parent_node)
    return ParentNode(tag = "div", children = nested_nodes)

def text_to_children(text: str, block_type: BlockType)-> list[HTMLNode]:
    strip_header: dict[BlockType, Callable[[str], str]] = {
            BlockType.HEADING        : lambda x: x.lstrip("#").lstrip(" "),
            BlockType.QUOTE          : lambda x: x.lstrip(">").strip(" "),
            BlockType.UNORDERED_LIST : lambda x: x.strip(),
            BlockType.ORDERED_LIST   : lambda x: x.strip(),
            BlockType.PARAGRAPH      : lambda x: x.strip(),
        }
    strip_list_header: dict[BlockType, Callable[[str], str]] = {
            BlockType.ORDERED_LIST   : lambda x: x[3:].strip(),
            BlockType.UNORDERED_LIST : lambda x: x.lstrip("- ").strip(),
        }
    text = strip_header[block_type](text)

    if (block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST):
        html_node_list: list[HTMLNode] = []
        for line in text.split("\n"):
            line = strip_list_header[block_type](line)
            node_list: list[TextNode] = text_to_textnodes(line)
            children: list[HTMLNode] = [text_node_to_html_node(node) for node in node_list]
            html_node_list.append(ParentNode(tag = "li", children = children))
        return html_node_list
    else:
        node_list = text_to_textnodes(text)
        html_node_list: list[HTMLNode] = [text_node_to_html_node(node) for node in node_list]
        return html_node_list

