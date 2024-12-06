import os
import shutil

def organize_doc(file_path, sender_folder, category):
    try:
        if category == "unknown" or category == "error":
            dest_folder = os.path.join(sender_folder, "uncategorized")
        else:
            dest_folder = os.path.join(sender_folder, category)
        
        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_folder, os.path.basename(file_path)))
        print(f"Arquivo movido para: {dest_folder}")
    except Exception as e:
        print(f"Erro ao organizar o arquivo {file_path}: {e}")
