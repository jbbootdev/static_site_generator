# python
import os
import shutil

from file_utilities import generate_pages_recursive


ROOT = os.path.dirname(os.path.dirname(__file__))
PUBLIC = os.path.join(ROOT, "public")
STATIC = os.path.join(ROOT, "static")
CONTENT_DIR = os.path.join(ROOT, "content")
DEST_DIR = os.path.join(ROOT, "public")
TEMPLATE = os.path.join(ROOT, "template.html")

def clean_public():
    if os.path.exists(PUBLIC):
        shutil.rmtree(PUBLIC)
    os.makedirs(PUBLIC, exist_ok=True)

def copy_static():
    # copies static/ into public/
    shutil.copytree(STATIC, PUBLIC, dirs_exist_ok=True)

def main():
    clean_public()
    copy_static()
    generate_pages_recursive(CONTENT_DIR, TEMPLATE, DEST_DIR)

if __name__ == "__main__":
    main()
