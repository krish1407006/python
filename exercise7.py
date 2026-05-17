# merge pdf using PyPDF2

from PyPDF2 import PdfMerger
def merge_pdfs(pdf_list, output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()

if __name__ == "__main__":

    pdf_list = ["file1.pdf", "file2.pdf", "file3.pdf"]  # replace with your pdf file names
    output = "merged.pdf"  # name of the output merged pdf
    merge_pdfs(pdf_list, output)
    print("PDFs merged successfully into", output)

