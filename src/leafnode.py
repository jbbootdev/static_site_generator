
# python
VOID_TAGS = {"img", "br", "hr", "meta", "link", "input", "source"}
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag=tag, value=value, props=props or {})

    def to_html(self):
        if self.tag is None:
            if self.value is None:
                raise ValueError("LeafNode with no tag must have value")
            return self.value

        attrs = "".join(f' {k}="{v}"' for k, v in self.props.items())

        if self.tag in VOID_TAGS:
            return f"<{self.tag}{attrs}>"

        if self.value is None:
            raise ValueError(f"LeafNode <{self.tag}> needs a value")

        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
