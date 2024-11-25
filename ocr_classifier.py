import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Seminario4\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
print(pytesseract.get_tesseract_version())
from pdf2image import convert_from_path

keywords = {
    "passport": ["パスポート", "pasaporte", "passport", "passaporte"],
    "insurance": ["保険加入", "seguro", "insurance", "seguro de saúde", "確保", "Cobertura", "coverage", "保険"],
    "id_card": ["身分証", "documento de identidad", "identification", "identidade"],
    "vaccine_certificate": ["予防接種証明書", "certificado de vacunación", "vaccination certificate", "certificado de vacinação"]
}

def analisar_e_classificar_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    texto_extraido = ""
    for page in pages:
        texto_extraido += pytesseract.image_to_string(page, lang="jpn+spa+por+eng")
    
    for categoria, palavras in keywords.items():
        for palavra in palavras:
            if palavra.lower() in texto_extraido.lower():
                return categoria  
    return "unknown"
