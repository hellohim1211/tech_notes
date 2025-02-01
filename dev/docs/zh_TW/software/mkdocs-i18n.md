# Setting Up Multilingual Support in MkDocs (English and Traditional Chinese)

## Prerequisites
```bash
pip install mkdocs-static-i18n
pip install jieba  # For better Chinese word segmentation
```

## Basic Configuration
### mkdocs.yml
```yaml
# Site information
site_name: Your Site Name
site_url: https://your-site.com/

# i18n Configuration
plugins:
  - search:
      lang:
        - en
        - zh
  - i18n:
      default_language: en
      languages:
        en:
          name: English
          build: true
        zh-tw:
          name: 繁體中文
          build: true
      nav_translations:
        zh-tw:
          Home: 首頁
          Getting Started: 開始使用
          Installation: 安裝說明
          Features: 功能介紹
          Advanced: 進階設定
          Documentation: 文件

# Language Selector Configuration
extra:
  alternate:
    - name: English
      link: /en/ 
      lang: en
    - name: 繁體中文
      link: /zh/
      lang: zh

# Navigation Structure
nav:
  - Home: 
    - en/index.md
    - zh/index.md
  - Getting Started:
    - Installation: 
      - en/installation.md
      - zh/installation.md
    - Quick Start: 
      - en/quick-start.md
      - zh/quick-start.md
  - Features:
    - Overview: 
      - en/features/overview.md
      - zh/features/advanced.md
```

## Directory Structure
```
docs/
├── en/
│   ├── index.md
│   ├── installation.md
│   ├── quick-start.md
│   └── features/
│       ├── overview.md
│       └── advanced.md
├── zh-tw/
│   ├── index.md
│   ├── installation.md
│   ├── quick-start.md
│   └── features/
│       ├── overview.md
│       └── advanced.md
└── assets/
    └── images/
```

## Content Examples

### English (docs/en/index.md)
```markdown
---
title: Home
lang: en
hreflang: en
---

# Welcome to Our Documentation

This is the English version of our documentation.

## Getting Started

Please check our installation guide to begin...
```

### Traditional Chinese (docs/zh-tw/index.md)
```markdown
---
title: 首頁
lang: zh-tw
hreflang: zh-tw
---

# 歡迎使用我們的文件

這是繁體中文版本的文件。

## 開始使用

請查看我們的安裝指南以開始使用...
```

## Usage and Building

### Local Development
```bash
mkdocs serve
```

### Production Build
```bash
mkdocs build
```

## Key Features
- Language switcher
- Separate URLs for each language (`/en/`, `/zh-tw/`)
- SEO-friendly configuration
- Multi-language search support
- Translated navigation
- Organized content structure

## URL Structure
- English: `https://your-site.com/en/`
- Traditional Chinese: `https://your-site.com/zh-tw/`

## Additional SEO Optimization
Add language meta tags in markdown files:
```markdown
---
lang: zh-tw
hreflang: zh-tw
description: 頁面描述
---
```

This configuration provides a professional multilingual documentation setup that's both user-friendly and SEO-optimized.