import PyPDF2
import sys
import os

class PDFProcessor:

    @staticmethod
    def add_whitespace(input_pdf_path, output_pdf_path, side = None) -> None:
    # Open the source PDF
        with open(input_pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            writer = PyPDF2.PdfWriter()
            for page_num in range(len(reader.pages)):
                # Extract each page
                page = reader.pages[page_num]
                # Rotate to 0 deg and simplify calcs
                deg = page.get('/Rotate')
                if deg not in [0, None]:
                    page.rotate(-deg)

                # Check if original is in landscape mode
                width, height = float(page.mediabox.width), float(page.mediabox.height)
                new_page = PDFProcessor._create_blank_page(width, height)
                new_page.merge_page(page)

                # Rotate back
                if deg not in [0, None]:
                    new_page.rotate(deg)
                writer.add_page(new_page)

            # Write the new modified PDF to a new file
            with open(output_pdf_path, 'wb') as out:
                writer.write(out)
    
    @staticmethod
    def _create_blank_page(orig_width: float, orig_height: float):
        if orig_width < orig_height:
            new_width, new_height = 1.33 * orig_width, orig_height
        else:
            new_width, new_height = orig_width, 1.33 * orig_height

        return PyPDF2._page.PageObject.create_blank_page(None, new_width, new_height)

    @staticmethod
    def check_page_is_portrait(page: PyPDF2.PageObject) -> bool:
        width = page.mediabox.width
        height = page.mediabox.height
        deg = page.get('/Rotate')
        return ((width <= height) and (deg not in [0,180,None]))
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: python {sys.argv[0]} input_file1 [input_file2 ...] /path_to_output_directory/")
        sys.exit(1)
    
    # The last argument is the output directory, all preceding arguments are input files.
    output_directory = sys.argv[-1]
    input_files = sys.argv[1:-1]
    
    for input_file in input_files:
        # Create the output path by joining the output directory with the input filename (without extension) + ".pdf"
        output_file = os.path.join(output_directory, os.path.splitext(os.path.basename(input_file))[0] + ".pdf")
        print(f"Input: {input_file}, Output: {output_file}")
        PDFProcessor.add_whitespace(input_file, output_file)

