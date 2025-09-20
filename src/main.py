# python
import os
import shutil
import sys

from file_utilities import generate_pages_recursive


ROOT = os.path.dirname(os.path.dirname(__file__))
DOCS_DIR = os.path.join(ROOT, "docs")
STATIC = os.path.join(ROOT, "static")
CONTENT_DIR = os.path.join(ROOT, "content")
DEST_DIR = os.path.join(ROOT, "public")
TEMPLATE = os.path.join(ROOT, "template.html")

def clean_docs():
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR, exist_ok=True)

def copy_static():
    shutil.copytree(STATIC, DOCS_DIR, dirs_exist_ok=True)

def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"
    clean_docs()
    copy_static()
    generate_pages_recursive(CONTENT_DIR, TEMPLATE, DEST_DIR, base_path)

if __name__ == "__main__":
    main()
