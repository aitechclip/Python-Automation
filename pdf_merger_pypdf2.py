import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_dir, output_filename):
    merger = PdfMerger()

    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            merger.append(pdf_path)

    merger.write(output_filename)
    merger.close()

if __name__ == "__main__":
    input_directory = "/path/to/pdf/files"  # Customize the input directory
    output_filename = "merged.pdf"  # Customize the output filename

    merge_pdfs(input_directory, output_filename)
