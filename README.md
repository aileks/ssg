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
- Copies static assets (CSS, images, etc.)
- Built-in web server for local testing

## Installation

- Python 3.11 or higher

## Usage

### Generate and serve the site locally

```bash
./main.sh
```

This will:

1. Copy all static files from `static/` to `public/`
2. Generate HTML pages from Markdown files in `content/`
3. Start a local web server at `http://localhost:8888`

### Run Tests

Run the test suite with `./test.sh`:

```bash
./test.sh
```
