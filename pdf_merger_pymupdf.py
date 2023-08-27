import os
import fitz  # PyMuPDF library

def merge_pdfs(input_dir, output_filename):
    pdfs = []

    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            pdfs.append(pdf_path)

    pdf_document = fitz.open()
    for pdf in pdfs:
        pdf_document.insert_pdf(fitz.open(pdf))

    pdf_document.save(output_filename)
    pdf_document.close()

if __name__ == "__main__":
    input_directory = "/path/to/pdf/files"  # Customize the input directory
    output_filename = "merged.pdf"  # Customize the output filename

    merge_pdfs(input_directory, output_filename)
