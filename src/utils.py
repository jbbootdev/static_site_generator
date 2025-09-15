# python

from unittest.runner import TextTestResult
from textnode import TextType, TextNode


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
