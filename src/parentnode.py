# python

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag=tag, children=children, props=props or {})

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None:
            raise ValueError("Children are required")

        attrs = "".join(f' {k}="{v}"' for k, v in self.props.items())
        inner = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{attrs}>{inner}</{self.tag}>"
