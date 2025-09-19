import os
import shutil

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


def sync_static_to_public(src: str="static", dest: str="public"):

    print("MADE IT HERE")
    if os.path.abspath(src) == os.path.abspath(dest):
        raise ValueError("Source and destination must be different directories.")

    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(f"deleted: {dest}")
        
    copy_recursive(src, dest)
    print("sync complete")
