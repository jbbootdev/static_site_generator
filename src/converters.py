# python
from block_type import BlockType
from parentnode import ParentNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from utils import (
    block_to_block,
    split_nodes_delimiter,
    split_nodes_link,
    split_nodes_image,
    markdown_to_blocks,
)
from typing import List


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block(block)

        if block_type == BlockType.PARAGRAPH:
            block_nodes.append(create_paragraph_html_node(block))

        if block_type == BlockType.CODE:
           block_nodes.append(create_code_html_block(block))

        if block_type == BlockType.QUOTE:
            block_nodes.append(create_block_quote_html_node(block))

        if block_type == BlockType.HEADING:
            lines = block.splitlines(True)
            for line in lines:
                stripped_line = line.lstrip()
                i = 0
                while i < len(stripped_line) and i < 6 and stripped_line[i] == "#":
                    i += 1
                level = i

                if i == 0 or i > 6 or (len(stripped_line) <= i or stripped_line[i] != " "):
                    continue

                heading_text = stripped_line[i+1:].rstrip("\n")
                text_nodes = text_to_textnodes(heading_text)
                children = [text_node_to_html_node(n) for n in text_nodes]
                block_nodes.append(ParentNode(tag=f"h{level}", children = children))

        if block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
            block_nodes.append(create_list_html_node(block))


    return ParentNode(tag="div", children = block_nodes) 


def create_list_html_node(block: str)->ParentNode:
    lines = block.splitlines(True)
    items = []
    complete_node = None
    for line in lines:
        stripped_line = line.lstrip()
        
        if stripped_line.startswith("- ") or stripped_line.startswith("* "):
            item_text = stripped_line[2:].rstrip("\n")
            tnodes = text_to_textnodes(item_text)
            children = [text_node_to_html_node(n) for n in tnodes]
            items.append(ParentNode(tag="li", children = children))
            complete_node = ParentNode(tag="ul", children=items)
        else:
            stripped_line = line.lstrip()
            i = 0
            while i < len(stripped_line) and stripped_line[i].isdigit():
                i += 1
            if i > 0 and i + 1 < len(stripped_line) and stripped_line[i] == "." and stripped_line[i+1] == " ":
                item_text = stripped_line[i+2:].rstrip("\n")
                tnodes = text_to_textnodes(item_text)
                children = [text_node_to_html_node(n) for n in tnodes]
                items.append(ParentNode("li", children=children))
                complete_node = ParentNode("ol", children = items)

    return complete_node


def create_block_quote_html_node(block: str) -> ParentNode:
    lines = block.splitlines(True)
    cleaned_lines = []
    for line in lines:
        line_stripped = line.lstrip()
        if not line_stripped.startswith(">"):
            continue

        content =line_stripped[1:]
        if content.startswith(" "):
            content = content[1:]

        content = content.rstrip("\n")
        if content.strip():
            cleaned_lines.append(content)

    quote_text = " ".join(cleaned_lines)
    children = [text_node_to_html_node(n) for n in text_to_textnodes(quote_text)]

    return ParentNode("blockquote", children=children)

def create_code_html_block(block: str)-> ParentNode:
    code = block.splitlines(True)
    code_text = code[1:-1]
    c = "".join(code_text)
    leaf_node = LeafNode(tag="code", value = c)
    return ParentNode(tag="pre", children = [leaf_node])


def create_paragraph_html_node(block: str)-> ParentNode:
    para_text = block.replace("\n", " ")
    text_nodes = text_to_textnodes(para_text)
    children = [text_node_to_html_node(n) for n in text_nodes]
    return ParentNode(tag="p", children = children)

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
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # 2) Structural markdown
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    # 3) Inline emphasis
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes
