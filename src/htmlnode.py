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




