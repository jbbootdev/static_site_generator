# python
import os
from converters import markdown_to_html_node


def extract_title(markdown: str):
    for line in markdown.splitlines():
        stripped_line = line.lstrip()
        if stripped_line.startswith("# ") and not stripped_line.startswith("##"):
            title = stripped_line[2:].strip()
            return title
    raise ValueError("No title provided.")

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as f:
        md = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    page = template.replace("{{ TITLE }}", title).replace("{{ Content }}", html).replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page)

