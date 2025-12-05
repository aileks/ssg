import sys
from copy_static import copy_static
from generate_pages import generate_pages_recursive


def main():
    # Get basepath from CLI argument, default to /
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_static()
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
