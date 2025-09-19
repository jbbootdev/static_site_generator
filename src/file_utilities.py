import os
import shutil
from pathlib import Path
from gen_content import generate_page

def copy_recursive(src: str, dest: str):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for entry in os.listdir(src):
        source_path = os.path.join(src, entry)
        destination_path = os.path.join(dest, entry)

        if os.path.isdir(source_path):
            copy_recursive(source_path, destination_path)
        else:
            shutil.copy2(source_path, destination_path)
            print(f"copied: {destination_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_root = Path(dir_path_content).resolve()
    dest_root = Path(dest_dir_path).resolve()
    template_path = Path(template_path).resolve()
    if not content_root.exists(): 
        raise FileNotFoundError(f"Content directory not found: {content_root}")

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    for md_path in content_root.rglob("*"):
        if md_path.is_file() and md_path.suffix.lower() == ".md":
            rel = md_path.relative_to(content_root)
            dest_html = dest_root / rel.with_suffix(".html")
            dest_html.parent.mkdir(parents=True, exist_ok=True)
            print("REL: ", rel)
            print("DEST HTML: ", dest_html)
            generate_page(md_path, template_path, dest_html)


def sync_static_to_public(src: str="static", dest: str="public"):

    print("MADE IT HERE")
    if os.path.abspath(src) == os.path.abspath(dest):
        raise ValueError("Source and destination must be different directories.")

    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(f"deleted: {dest}")
        
    copy_recursive(src, dest)
    print("sync complete")
