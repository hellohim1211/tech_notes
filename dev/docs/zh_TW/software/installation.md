# zh-tw Installation Guide

Getting started with MkDocs is straightforward. This guide will walk you through the installation process and initial setup.

## Prerequisites

Before installing MkDocs, ensure you have:

- Python 3.6 or later
- pip (Python package installer)

## Installation Steps

### 1. Install MkDocs

```bash
pip install mkdocs
```

### 2. Install Material Theme

```bash
pip install mkdocs-material
```

### 3. Verify Installation

```bash
mkdocs --version
```

## Creating Your First Project

### 1. Create a New Project

```bash
mkdocs new my-docs
cd my-docs
```

This will create a new directory with the following structure:

```
my-docs/
├── docs/
│   └── index.md
└── mkdocs.yml
```

### 2. Start the Development Server

```bash
mkdocs serve
```

!!! success "Development Server"
    Your documentation site should now be available at `http://127.0.0.1:8000`

## Next Steps

After installation, you should:

1. Configure your `mkdocs.yml` file
2. Add content to your documentation
3. Customize your theme

Check out the [Basic Configuration](basic-configuration.md) guide to learn more about setting up your documentation site.