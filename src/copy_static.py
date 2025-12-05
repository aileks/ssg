import os
import shutil


def copy_static():
    source = "static"
    dest = "docs"

    # Delete the docs directory if it exists
    if os.path.exists(dest):
        print(f"Removing directory: {dest}")
        shutil.rmtree(dest)

    # Create the docs directory
    os.mkdir(dest)
    print(f"Created directory: {dest}")

    # Recursively copy all files
    copy_directory_contents(source, dest)


def copy_directory_contents(src, dst):
    for filename in os.listdir(src):
        src_path = os.path.join(src, filename)
        dst_path = os.path.join(dst, filename)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"Creating directory: {dst_path}")
            os.mkdir(dst_path)
            copy_directory_contents(src_path, dst_path)
