import fitz  
import os

pdf_folder = "data/pdfs/"
output_folder = "data/"

all_text = []

for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        all_text.append(text)

full_text = "\n".join(all_text)

with open(os.path.join(output_folder, "raw_text.txt"), "w", encoding="utf-8") as f:
    f.write(full_text)

print("PDF text extracted and saved as raw_text.txt")
