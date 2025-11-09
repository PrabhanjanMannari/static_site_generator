from __future__ import annotations 
from enum import Enum
from dataclasses import dataclass

class TextType(Enum):
    TEXT   = "text"
    BOLD   = "bold text"
    ITALIC = "italic text"
    CODE   = "code text"
    LINK   = "link"
    IMAGE  = "image"

@dataclass
class TextNode():
    text: str           = None
    text_type: TextType = TextType.TEXT
    url: str            = None

    def __eq__(self, other: TextNode)-> bool:
        return (self.text == other.text) and (self.text_type == other.text_type) and (self.url == other.url)

    def __repr__(self)-> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

