import os

def organize_doc(anexo_path, sender_folder, categoria):
    pasta_categoria = os.path.join(sender_folder, categoria)
    os.makedirs(pasta_categoria, exist_ok=True)
    novo_caminho = os.path.join(pasta_categoria, os.path.basename(anexo_path))
    os.rename(anexo_path, novo_caminho)
