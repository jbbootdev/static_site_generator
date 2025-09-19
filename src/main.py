# python
import os
import shutil

from gen_content import generate_page

ROOT = os.path.dirname(os.path.dirname(__file__))
PUBLIC = os.path.join(ROOT, "public")
STATIC = os.path.join(ROOT, "static")
CONTENT_MD = os.path.join(ROOT, "content", "index.md")
TEMPLATE = os.path.join(ROOT, "template.html")
DEST_HTML = os.path.join(PUBLIC, "index.html")

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
    generate_page(CONTENT_MD, TEMPLATE, DEST_HTML)

if __name__ == "__main__":
    main()
