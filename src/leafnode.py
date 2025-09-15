# python
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError()

        if self.tag is None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
