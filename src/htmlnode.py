# python


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        string_parts = []

        if self.props:
            for key, value in self.props.items():
                string_parts.append(f' {key}="{value}"')

        return "".join(string_parts)
