from pypdf import PdfReader

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)   # ✅ create reader object
    text_data = ""

    for page in reader.pages:      # ✅ use reader.pages
        content = page.extract_text()
        if content:
            text_data += content + "\n"

    return text_data
