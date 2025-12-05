from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_nodes = split_text_node(node, delimiter, text_type)
            new_nodes.extend(split_nodes)

    return new_nodes


def split_text_node(node, delimiter, text_type):
    parts = node.text.split(delimiter)

    # Check for odd number of parts (valid markdown)
    if len(parts) % 2 == 0:
        raise ValueError(f"Invalid markdown: unclosed delimiter '{delimiter}'")

    new_nodes = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            # Even index = text type
            if part:  # Only add non-empty text nodes
                new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            # Odd index = specified type
            new_nodes.append(TextNode(part, text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if not images:
                new_nodes.append(node)
            else:
                text = node.text
                for alt_text, image_url in images:
                    # Split on the image markdown
                    sections = text.split(f"![{alt_text}]({image_url})", 1)

                    # Add the text before the image
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))

                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))

                    # Keep the rest for next iteration
                    text = sections[1]

                # Add any remaining text after the last image
                if text:
                    new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if not links:
                new_nodes.append(node)
            else:
                text = node.text
                for link_text, link_url in links:
                    # Split on the link markdown
                    sections = text.split(f"[{link_text}]({link_url})", 1)

                    # Add the text before the link
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))

                    new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

                    # Keep the rest for next iteration
                    text = sections[1]

                # Add any remaining text after the last link
                if text:
                    new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    # Filter out empty text nodes
    nodes = [node for node in nodes if node.text]

    return nodes
