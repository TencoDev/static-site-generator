# Static Site Generator V1

A lightweight, custom-built static site generator that transforms Markdown content into HTML websites.

This demo site was built using this!
🔗 [Live Demo: Kantodex](https://tencodev.github.io/static-site-generator/#kantodex)

## Overview

This project is a from-scratch implementation of a static site generator, built to convert Markdown files into a fully functional static website. It takes content from `.md` files and transforms them into HTML, maintaining a clean directory structure while preserving static assets.

## Features

- **Markdown to HTML conversion** - Transform content written in Markdown into structured HTML
- **Static asset handling** - Properly manages images, CSS, and other static files
- **Simple project structure** - Organized content management system
- **Zero dependencies** - Built from the ground up with vanilla code
- **Fast build times** - Lightweight implementation for quick generation
- **Custom routing** - URL-friendly navigation structure
- **Live demo example** - Kantodex showcase demonstrates the generator in action

## Project Structure

```
static-site-generator/
├── content/           # Source Markdown files
├── static/            # Static assets (CSS, images, etc.)
├── docs/              # Output directory with generated HTML
└── src/               # Source code for the generator
```

## How It Works

1. The generator scans the `content/` directory for Markdown files
2. It processes each file, converting Markdown syntax to HTML
3. Static assets from the `static/` directory are copied to the output location
4. The complete site is output to the `docs/` directory, ready for deployment

## Getting Started

### Prerequisites

- Python installed on your system

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TencoDev/static-site-generator.git
cd static-site-generator
```

### Usage

Run the generator:

```bash
./main.sh
```

This will process all Markdown files and generate your static site in the `docs/` directory.

## Customization

You can customize the appearance of the generated site by modifying the templates and CSS files in the `static/` directory and `content/` directory.

## Demo: Kantodex

The [Kantodex demo](https://tencodev.github.io/static-site-generator/#kantodex) showcases what this static site generator can produce. It demonstrates the conversion capabilities from Markdown source files to a functional HTML website.

## Current Limitations

- Limited table support
- Nested inline elements not fully supported
- No built-in templating system

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

[MIT License](LICENSE)

## Author

[TencoDev](https://github.com/TencoDev)