import pytesseract
from pdf2image import convert_from_path

# Configurar o caminho para o Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Seminario4\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Palavras-chave para classificar documentos
keywords = {
    "passport": ["パスポート", "pasaporte", "passport", "passaporte"],
    "insurance": ["保険加入", "seguro", "insurance", "seguro de saúde", "確保", "Cobertura", "coverage", "保険"],
    "id_card": ["身分証", "documento de identidad", "identification", "identidade"],
    "vaccine_certificate": ["予防接種証明書", "certificado de vacunación", "vaccination certificate", "certificado de vacinação"]
}

def analisar_e_classificar_pdf(pdf_path):
    try:
        pages = convert_from_path(pdf_path)  # Converte as páginas do PDF para imagens
        texto_extraido = ""
        for page in pages:
            texto_extraido += pytesseract.image_to_string(page, lang="jpn+spa+por+eng")
        
        # Verificar palavras-chave
        for categoria, palavras in keywords.items():
            for palavra in palavras:
                if palavra.lower() in texto_extraido.lower():
                    return categoria  # Retorna a categoria correspondente
        return "unknown"  # Se nenhuma palavra-chave for encontrada
    except Exception as e:
        print(f"Erro ao processar PDF: {pdf_path} - {e}")
        return "error"
