import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, "r") as f:
        markdown = f.read()

    # Read the template file
    with open(template_path, "r") as f:
        template = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    # Extract the title
    title = extract_title(markdown)

    # Replace placeholders
    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)

    # Replace basepath in href and src attributes
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    # Create directories if needed
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Write to destination file
    with open(dest_path, "w") as f:
        f.write(html)
