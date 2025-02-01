import yaml
import os


def create_markdown_file(file_path, title):
    """Create a markdown file with basic content"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        # 創建基本的 markdown 內容
        content = f"""# {title}

## Overview

Content for {title} goes here.


"""
        f.write(content)
    print(f"Created file: {file_path}")


def process_nav_item(item, docs_dir):
    """Recursively process nav items and create directories and files"""
    if isinstance(item, dict):
        for section_name, content in item.items():
            if isinstance(content, (list, dict)):
                process_nav_item(content, docs_dir)
            elif isinstance(content, str) and content.endswith('.md'):
                file_path = os.path.join(docs_dir, content)
                title = section_name.replace('-', ' ').title()
                create_markdown_file(file_path, title)
    elif isinstance(item, list):
        for sub_item in item:
            process_nav_item(sub_item, docs_dir)


def create_docs_structure(yaml_path):
    """Main function to create documentation structure"""
    # 讀取 YAML 文件
    with open(yaml_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # 確定 docs 目錄的位置（假設在當前目錄下）
    docs_dir = 'docs'
    os.makedirs(docs_dir, exist_ok=True)

    # 創建 index.md
    index_content = """# Welcome to the Documentation

## Getting Started

- [Installation](installation.md)
- [Basic Configuration](basic-configuration.md)
- [Themes](themes.md)

## Overview

This documentation covers various topics including software installation, 
programming languages, and AI/ML concepts.

## Navigation

Use the navigation menu on the left to browse through different sections.
"""
    with open(os.path.join(docs_dir, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Created index.md")

    # 處理導航部分
    if 'nav' in config:
        process_nav_item(config['nav'], docs_dir)
        print("Documentation structure created successfully!")
    else:
        print("No 'nav' section found in the YAML file.")


if __name__ == "__main__":
    # 使用 nav.yml
    yaml_path = "nav.yml"

    if os.path.exists(yaml_path):
        create_docs_structure(yaml_path)
    else:
        print(f"Error: {yaml_path} not found!")
