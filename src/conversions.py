from enum import Enum

import re 

from textnode import *
from htmlnode import *

class BlockType(Enum):
    PARAGRAPH      = "PARAGRAPH"
    HEADING        = "HEADING"
    CODE           = "CODE"
    QUOTE          = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST   = "ORDERED_LIST"

def text_node_to_html_node(text_node: TextNode)-> LeafNode:
    tag: str   = text_node.text_type.tag()
    value: str = text_node.text
    props: str = None
    if (text_node.text_type == TextType.UNKNOWN):
        raise TypeError("text_node has unknown text_type")

    if (text_node.text_type == TextType.LINK):
        props = {"href" : text_node.url}
    elif(text_node.text_type == TextType.IMAGE):
        value = ""
        props = {"src" : text_node.url, "alt" : text_node.text}

    return LeafNode(tag = tag, value = value, props = props)

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType)-> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if (node.text_type != TextType.TEXT):
            new_nodes.append(node)
        else: 
            parts: list[str] = node.text.split(delimiter)
            if (len(parts) % 2 == 0):
                raise TypeError(f"Matching delimiter not found in {node.text}")

            node_list: list[TextNode] = []
            isText = True 
            for part in parts:
                if (len(part) == 0):
                    isText = isText ^ True
                    continue 
                if (isText):
                    node_list.append(TextNode(part, TextType.TEXT))
                else:
                    node_list.append(TextNode(part, text_type))
                isText = isText ^ True 
            new_nodes.extend(node_list)
    return new_nodes

def extract_markdown_images(text: str)->list[tuple[str]]:
    image_regex: str = r"!\[(.*?)]\((.*?)\)"
    return re.findall(image_regex, text)

def extract_markdown_links(text: str)->list[tuple[str]]:
    link_regex: str = f"(?<!!)\[(.*?)\]\((.*?)\)"
    return re.findall(link_regex, text)

def split_nodes_image(old_nodes: list[TextNode])-> list[TextNode]:
    image_regex: str = r"!\[(.*?)]\((.*?)\)"
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if (node.text_type == TextType.TEXT):
            node_list: list[TextNode] = []
            parsedTill: int = 0

            for match in re.finditer(image_regex, node.text):
                if (match.start() > parsedTill):
                    text_part: str = node.text[parsedTill : match.start()]
                    node_list.append(TextNode(text_part, TextType.TEXT))

                node_list.append(TextNode(match.group(1), TextType.IMAGE, match.group(2)))
                parsedTill = match.end()

            if (parsedTill < len(node.text)):
                node_list.append(TextNode(node.text[parsedTill:]))

            new_nodes.extend(node_list)
        else: 
            new_nodes.append(node)

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode])-> list[TextNode]:
    link_regex: str = f"(?<!!)\[(.*?)\]\((.*?)\)"
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if (node.text_type == TextType.TEXT):
            node_list: list[TextNode] = []
            parsedTill: int = 0

            for match in re.finditer(link_regex, node.text):
                if (match.start() > parsedTill):
                    text_part: str = node.text[parsedTill : match.start()]
                    node_list.append(TextNode(text_part, TextType.TEXT))

                node_list.append(TextNode(match.group(1), TextType.LINK, match.group(2)))
                parsedTill = match.end()

            if (parsedTill < len(node.text)):
                node_list.append(TextNode(node.text[parsedTill:]))

            new_nodes.extend(node_list)
        else: 
            new_nodes.append(node)

    return new_nodes

def text_to_textnodes(text: str)-> list[TextNode]:
    node_list: list[TextNode] = [TextNode(text)]
    
    node_list = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    node_list = split_nodes_delimiter(node_list, "_", TextType.ITALIC)
    node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)

    node_list = split_nodes_image(node_list)
    node_list = split_nodes_link(node_list)

    return node_list

def markdown_to_blocks(markdown: str)-> list[str]:
    blocks: list[str] = []
    preprocessed_markdown: list[str] = [block.strip("\n").strip() for block in markdown.split("\n\n")]
    for block in preprocessed_markdown:
        if (len(block) == 0):
            continue 
        blocks.append(block)
    return blocks 

def block_to_block_type(block: str)-> BlockType:
    # heading check 
    if (block[0] == "#"):
        idx = 1
        header_len = min(len(block), 6)
        while (idx < header_len):
            if (block[idx] != "#"):
                break 
            idx += 1
        if (idx < len(block) and block[idx] == " "):
            return BlockType.HEADING

    # code check 
    if (len(block) >= 6 and block[:3] == "```" and block[-3:] == "```"): 
        return BlockType.CODE

    lines = block.split("\n")

    # quote check 
    isQuote: bool = True 
    for line in lines:
        if (line[0] != ">"):
            isQuote = False 
            break 
    if (isQuote):
        return BlockType.QUOTE

    # unordered list check 
    isUnorderedList: bool = True 
    for line in lines:
        if (len(line) < 2 or line[:2] != "- "):
            isUnorderedList = False 
            break 
    if (isUnorderedList):
        return BlockType.UNORDERED_LIST

    # ordered list check 
    isOrderedList: bool = True 
    for num, line in enumerate(lines):
        if (len(line) < 3 or line[:3] != f"{num + 1}. "):
            isOrderedList = False 
            break 
    if (isOrderedList):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
