from copy_static import copy_static
from generate_pages import generate_pages_recursive


def main():
    copy_static()
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
