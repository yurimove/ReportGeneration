import os
from fpdf import FPDF
from docx import Document

def file_to_pdf(input_file):
    # Check if the file exists
    if not os.path.isfile(input_file):
        print("❌ File not found!")
        return

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # File extension
    ext = os.path.splitext(input_file)[1].lower()

    if ext == ".txt":
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                pdf.multi_cell(0, 10, line.strip())
    elif ext == ".docx":
        doc = Document(input_file)
        for para in doc.paragraphs:
            text = para.text.strip()
            if text:
                pdf.multi_cell(0, 10, text)
    else:
        print("❌ Unsupported file type! Please use a .txt or .docx file.")
        return

    # Dynamic output file name
    output_pdf = os.path.splitext(input_file)[0] + ".pdf"
    pdf.output(output_pdf)
    print(f"✅ PDF successfully created: {output_pdf}")

# 🖋️ Ask user for file name
file_name = input("Enter the file name (with .txt or .docx): ")
file_to_pdf(file_name)
