import os 
import shutil

from html_conversions import *

def refresh_util(src: str, dest: str)-> None:
    def copy_files(src: str, dest: str):
        for file in os.listdir(src):
            file_path: str = os.path.join(src, file)
            if (os.path.isfile(file_path)):
                shutil.copy(file_path, dest)
            else:
                dest_dir: str = os.path.join(dest, file)
                if (not os.path.exists(dest_dir)):
                    os.mkdir(dest_dir)
                copy_files(file_path, dest_dir)

    for path in os.listdir(dest):
        file_path: str = os.path.join(dest, path)
        if (not os.path.isfile(file_path)):
            shutil.rmtree(file_path)

    copy_files(src, dest)        


def extract_title(markdown)-> str:
    for line in markdown.split("\n"):
        if (len(line) >= 2 and line[:2] == "# "):
            return line.lstrip("# ").strip()
    raise ValueError("Unable to find the title field")

def generate_page(from_path: str = "content/index.md", 
                  template_path: str = "template.html", 
                  dest_path: str = "public/index.html", 
                  base_path: str = "/")-> None:

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown: str = f.read()
    with open(template_path, "r") as f:
        template: str = f.read()

    gen_html: str = markdown_to_html_node(markdown).to_html()
    title: str    = extract_title(markdown)
    
    total_html: str = template.replace("{{ Title }}", title)
    total_html      = total_html.replace("{{ Content }}", gen_html)

    total_html.replace('href="/', f'href="{base_path}')
    total_html.replace('src="/', f'src="{base_path}')

    with open(dest_path, "w") as f:
        f.write(total_html)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, base_path: str = "/")-> None:
    for file in os.listdir(dir_path_content):
        file_path: str = os.path.join(dir_path_content, file)
        if (os.path.isfile(file_path)):
            generate_page(file_path, template_path, os.path.join(dest_dir_path, f"{file.rstrip('md')}html"))
        else:
            dest_path = os.path.join(dest_dir_path, file)
            if (not os.path.exists(dest_path)):
                os.mkdir(dest_path)
            generate_pages_recursive(file_path, template_path, dest_path)

