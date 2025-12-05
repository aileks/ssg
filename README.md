# Static Site Generator (SSG)

A simple static site generator built in Python that converts Markdown files into HTML pages.

## Features

- Converts Markdown to HTML with support for:
  - Headings (h1-h6)
  - Bold and italic text
  - Code blocks and inline code
  - Links and images
  - Ordered and unordered lists
  - Block quotes
- Recursively generates pages from a content directory
- Copies static assets (CSS, images, etc.) to output directory
- Configurable basepath for deployment to subdirectories
- Built-in web server for local testing

## Installation

- Python 3.11 or higher

## Usage

### Generate and serve the site locally

```bash
./main.sh
```

This will:

1. Copy all static files from `static/` to `docs/`
2. Generate HTML pages from Markdown files in `content/` to `docs/`
3. Start a local web server at `http://localhost:8888` serving from `docs/`

### Build for deployment

To build with a custom basepath (e.g., for GitHub Pages):

```bash
./build.sh
```

This generates the site with basepath `/ssg/` (useful for deployment to subdirectories).

### Generate site programmatically

You can also run the generator directly:

```bash
python3 src/main.py [basepath]
```

- Without arguments: uses basepath `/` (default)
- With basepath argument: uses the specified basepath (e.g., `/my-site/`)

### Run Tests

Run the test suite with `./test.sh`:

```bash
./test.sh
```

This runs all unit tests using Python's unittest framework.

## Project Structure

- `content/` - Markdown source files
- `static/` - Static assets (CSS, images, etc.)
- `docs/` - Generated HTML output (served locally)
- `src/` - Python source code
- `template.html` - HTML template for generated pages
- `main.sh` - Script to generate and serve locally
- `build.sh` - Script to build with deployment basepath
