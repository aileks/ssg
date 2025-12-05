from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")
    
    # Check for heading
    if lines[0].startswith("#"):
        header_count = 0
        for char in lines[0]:
            if char == "#":
                header_count += 1
            else:
                break
        if 1 <= header_count <= 6 and lines[0][header_count] == " ":
            return BlockType.HEADING
    
    # Check for code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for quote
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list
    is_ordered_list = True
    for i, line in enumerate(lines):
        if not line.startswith(f"{i + 1}. "):
            is_ordered_list = False
            break
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    # Default to paragraph
    return BlockType.PARAGRAPH
