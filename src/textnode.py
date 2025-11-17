from __future__ import annotations 
from enum import Enum
from dataclasses import dataclass
from typing import Optional

class TextType(Enum):
    UNKNOWN = "UNKNOWN"
    TEXT    = "TEXT"
    BOLD    = "BOLD"
    ITALIC  = "ITALIC"
    CODE    = "CODE"
    ULIST   = "ULIST"
    OLIST   = "OLIST"
    LIST_EL = "LIST_EL"
    LINK    = "LINK"
    IMAGE   = "IMAGE"

    def tag(self)-> str:
        text_type_to_tag: dict[TextType, Optional[str]] = {
            TextType.TEXT    : None,
            TextType.BOLD    : "b",
            TextType.ITALIC  : "i",
            TextType.CODE    : "code",
            TextType.ULIST   : "ul",
            TextType.OLIST   : "ol",
            TextType.LIST_EL : "li",
            TextType.LINK    : "a",
            TextType.IMAGE   : "img",
        }
        return text_type_to_tag[self]

@dataclass
class TextNode():
    text: str           = None
    text_type: TextType = TextType.TEXT
    url: str            = None

    def __eq__(self, other: TextNode)-> bool:
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self)-> str:
        if (self.url is None):
            return f"TextNode('{self.text}', {self.text_type.value})"
        else:
            return f"TextNode('{self.text}', {self.text_type.value}, {self.url})"

