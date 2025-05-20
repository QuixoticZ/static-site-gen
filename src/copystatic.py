import os
import shutil
import re
from block_markdown import markdown_to_html_node
from pathlib import Path



dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    header = re.search(r"#.+(?:$|\n\n)",markdown)
    if header == None:
        raise Exception("No header found")
    return header.group(0)[1:]

def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path}, using {template_path}")

    mdfile = open(f"{from_path}","r")
    md_contents=mdfile.read()
    tmpfile = open(f"{template_path}","r+")
    mdfile.close()
    tmp_contents =tmpfile.read()
    tmpfile.close()
    
    markdown_html = markdown_to_html_node(md_contents).to_html()
    title = extract_title(md_contents)
    tmp_contents = tmp_contents.replace(f"{{{{ Title }}}}",title)
    tmp_contents = tmp_contents.replace(f"{{{{ Content }}}}",markdown_html)
    newfile = open(f"{dest_path}","x")
    newfile.write(tmp_contents)
    newfile.close()
    



