import os
from generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                # It's a markdown file, generate HTML
                # Replace .md extension with .html
                dest_path = dest_path.replace(".md", ".html")
                generate_page(from_path, template_path, dest_path)
        else:
            # It's a directory, recurse
            generate_pages_recursive(from_path, template_path, dest_path)
