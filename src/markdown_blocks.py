def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped:
            filtered_blocks.append(stripped)
    return filtered_blocks
