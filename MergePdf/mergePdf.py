import sys
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python mergePdf.py output.pdf input1.pdf input2.pdf [input3.pdf ...]")
        sys.exit(1)
    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    merge_pdfs(input_files, output_file)
    print(f"Merged PDFs saved as {output_file}")
