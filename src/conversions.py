from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node: TextNode)-> HTMLNode:
    tag: str   = text_node.text_type.tag()
    value: str  = text_node.text
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

                



    
    
