from __future__ import annotations 
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class HTMLNode():
    tag: str | None                    = None
    value: str | None                  = None
    children: Optional[List[HTMLNode]] = None
    props: Optional[Dict[str, str]]    = None
    
    def to_html(self):
        raise NotImplementedError("This option is not implemented yet")

    def props_to_html(self)-> str:
        if (self.props is None):
            return ""
        props_list: List[str] = []

        for key, value in self.props.items():
            props_list.append(f' {key}="{value}"')
        
        return "".join(props_list)


class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, 
                 children: Optional[List[HTMLNode]] = None, 
                 props: Optional[Dict[str, str]] = None)-> LeafNode:

        super().__init__(tag, value, children, props)

        if (self.value is None):
            raise ValueError("A LeafNode necessarily needs to have tag and value members")
        if (self.children is not None):
            raise ValueError("A LeafNode node should have no children: children parameter should be None")
        
    def to_html(self):
        if (self.tag is None):
            return self.value 
        html_start_tag = f"<{self.tag}{self.props_to_html()}>"
        html_end_tag   = f"</{self.tag}>"
        return f"{html_start_tag}{self.value}{html_end_tag}"


