import os
from datetime import date

def create_dated_folder(base_path="."):
    folder_name = date.today().strftime("%Y-%m-%d")
    full_path = os.path.join(base_path, folder_name)
    os.makedirs(full_path, exist_ok=True)
    print(f"Folder created: {full_path}")