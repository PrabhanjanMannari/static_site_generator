from __future__ import annotations 
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class HTMLNode():
    tag: str | None                    = None
    value: str | None                  = None
    children: Optional[list[HTMLNode]] = None
    props: Optional[dict[str, str]]    = None
    
    def to_html(self):
        raise NotImplementedError("This option is not implemented yet")

    def props_to_html(self)-> str:
        if (self.props is None):
            return ""
        props_list: list[str] = []

        for key, value in self.props.items():
            props_list.append(f' {key}="{value}"')
        
        return "".join(props_list)


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str,
                 children: Optional[list[HTMLNode]] = None, 
                 props: Optional[dict[str, str]] = None)-> LeafNode:

        super().__init__(tag, value, children, props)

        if (self.value is None):
            raise ValueError("A LeafNode necessarily needs to have tag and value members")
        if (self.children is not None):
            raise ValueError("A LeafNode node should have no children: children parameter should be None")
        
    def to_html(self)-> str:
        if (self.tag is None):
            return self.value 
        html_start_tag: str = f"<{self.tag}{self.props_to_html()}>"
        html_end_tag: str   = f"</{self.tag}>"
        return f"{html_start_tag}{self.value}{html_end_tag}"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: Optional[list[HTMLNode]] = None, 
                 value: str = None, props: Optional[dict[str, str]] = None)-> ParentNode:
        super().__init__(tag, value, children, props)

        if (self.value is not None):
            raise ValueError("A ParentNode should not have value member: value = None")
        if (self.tag is None or self.children is None):
            raise ValueError("A ParentNode necessarily needs to have tag and children members")

    def to_html(self)-> str:
        start_tag: str = f"<{self.tag}>"
        end_tag: str   = f"</{self.tag}>"

        html_content_list: list[str] = []

        for child in self.children:
            html_content_list.append(child.to_html())
        html_content = "".join(html_content_list)

        return f"{start_tag}{html_content}{end_tag}"
