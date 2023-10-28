from pdf_processor import PDFProcessor
import PyPDF2

input_pdf_path = "/Users/juliancolbert/Desktop/temp/14_C_Arrays_Pointers.pdf"

with open(input_pdf_path, 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    writer = PyPDF2.PdfWriter()
    mbox = reader.pages[0].mediabox
    for page_num in range(len(reader.pages)):
        # Extract each page
        page = reader.pages[page_num]
        is_portrait = PDFProcessor.check_page_is_portrait(page)
        print(f"Page {page_num}: width {mbox.width}, height {mbox.height} deg {page.get('/Rotate')}, is_portrait {is_portrait}")

