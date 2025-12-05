from textnode import TextNode, TextType


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
        raise ValueError(
            f"Invalid markdown: unclosed delimiter '{delimiter}'"
        )
    
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
