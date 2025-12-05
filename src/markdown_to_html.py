from markdown_blocks import markdown_to_blocks
from block_types import block_to_block_type, BlockType
from split_nodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import ParentNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_html_node(block, block_type)
        children.append(html_node)

    return ParentNode("div", children)


def block_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes


def paragraph_to_html_node(block):
    children = text_to_children(block)
    return ParentNode("p", children)


def heading_to_html_node(block):
    heading_level = 0
    for char in block:
        if char == "#":
            heading_level += 1
        else:
            break

    text = block[heading_level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{heading_level}", children)


def code_to_html_node(block):
    text = block[3:-3]

    lines = text.split("\n")

    if lines and lines[0].strip() and not lines[0].startswith(" "):
        lines = lines[1:]

    text = "\n".join(lines).strip() + "\n"

    code_node = TextNode(text, TextType.CODE)
    html_node = text_node_to_html_node(code_node)
    return ParentNode("pre", [html_node])


def quote_to_html_node(block):
    lines = block.split("\n")
    quote_lines = []

    for line in lines:
        if line.startswith("> "):
            quote_lines.append(line[2:])
        elif line.startswith(">"):
            quote_lines.append(line[1:])

    quote_text = "\n".join(quote_lines)
    children = text_to_children(quote_text)
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block):
    lines = block.split("\n")
    list_items = []

    for line in lines:
        item_text = line[2:]
        children = text_to_children(item_text)
        list_item = ParentNode("li", children)
        list_items.append(list_item)

    return ParentNode("ul", list_items)


def ordered_list_to_html_node(block):
    lines = block.split("\n")
    list_items = []

    for line in lines:
        dot_index = line.index(". ")
        item_text = line[dot_index + 2 :]
        children = text_to_children(item_text)
        list_item = ParentNode("li", children)
        list_items.append(list_item)

    return ParentNode("ol", list_items)
