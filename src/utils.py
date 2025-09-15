# python

from textnode import TextType, TextNode
from typing import List
import textwrap
import re


def markdown_to_blocks(markdown):
    md = textwrap.dedent(markdown).replace("\r\n", "\n").replace("\r", "\n").strip()
    raw_blocks = re.split(r"\n\s*\n", md)
    blocks = []
    for block in raw_blocks:
        if not block.strip():
            continue
        lines = [line.strip() for line in block.split("\n")]
        blocks.append("\n".join(lines))

    return blocks


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
        else:
            text_parts = node.text.split(delimiter)
            if len(text_parts) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            else:
                for index, part in enumerate(text_parts):
                    if part != "":
                        if index % 2 == 0:
                            new_node = TextNode(part, TextType.TEXT)
                            nodes.append(new_node)
                        else:
                            new_node = TextNode(part, text_type)
                            nodes.append(new_node)

    return nodes


IMAGE_RE = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")
LINK_RE = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")


def _split_by_pattern(old_nodes: List["TextNode"], pattern: re.Pattern, make_node):
    new_nodes: List["TextNode"] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        last = 0
        for m in pattern.finditer(text):
            start, end = m.span()

            if start > last:
                new_nodes.append(TextNode(text[last:start], TextType.TEXT))

            label = m.group(1)
            url = m.group(2)
            new_nodes.append(make_node(label, url))

            last = end

        # trailing text
        if last < len(text):
            new_nodes.append(TextNode(text[last:], TextType.TEXT))

    return new_nodes


def split_nodes_image(old_nodes: List["TextNode"]) -> List["TextNode"]:
    return _split_by_pattern(
        old_nodes,
        IMAGE_RE,
        lambda alt, url: TextNode(alt, TextType.IMAGE, url),
    )


def split_nodes_link(old_nodes: List["TextNode"]) -> List["TextNode"]:
    return _split_by_pattern(
        old_nodes,
        LINK_RE,
        lambda label, url: TextNode(label, TextType.LINK, url),
    )


def extract_markdown_images(text: str):
    return IMAGE_RE.findall(text)


def extract_markdown_links(text: str):
    return LINK_RE.findall(text)
