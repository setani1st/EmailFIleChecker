import os
import win32com.client
import pandas as pd
from ocr_classifier import analisar_e_classificar_pdf
from file_manager import organize_doc

def verify_email(excel_path, base_folder):
    df = pd.read_excel(excel_path)
    email_list = df['メール'].tolist()

    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    inbox = namespace.GetDefaultFolder(6)


    for message in inbox.Items:
        if message.Unread:
            sender_email = message.senderEmailAddress
            sender_name = message.SenderName

            if sender_email in email_list:
                #builds a new folder for the sender in order to save the files
                sender_folder = os.path.join(base_folder, sender_name)
                os.makedirs(sender_folder, exist_ok = True)

                for attachment in message.Attachments:
                    anexo_path = os.path.join(sender_folder, attachment.FileName)
                    attachment.SaveAsFile(anexo_path)
                    
                    # Chama OCR e classifica
                    categoria = analisar_e_classificar_pdf(anexo_path)
                    organize_doc(anexo_path, sender_folder, categoria)
                
                print(f"Documentos de {sender_name} foram salvos e organizados.")
                message.Unread = False  # Marca como lido após processamento