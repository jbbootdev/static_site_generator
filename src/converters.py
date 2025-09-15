# python
from leafnode import LeafNode
from textnode import TextNode, TextType
from utils import split_nodes_delimiter, split_nodes_link, split_nodes_image
from typing import List


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text)

    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", text_node.text)
    raise ValueError("unsupported TextType")


def text_to_textnodes(text: str) -> List["TextNode"]:
    """
    Convert a markdown-ish string into a flat list of TextNode objects by
    running all the splitters in precedence order.
    """
    nodes: List[TextNode] = [TextNode(text, TextType.TEXT)]

    # 1) Protect code spans so nothing else parses inside them
    nodes = split_nodes_delimiter("`", TextType.CODE, nodes)

    # 2) Structural markdown
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # 3) Inline emphasis
    nodes = split_nodes_delimiter("**", TextType.BOLD, nodes)
    nodes = split_nodes_delimiter("_", TextType.ITALIC, nodes)

    return nodes
