# from pdf2docx import Converter

# pdf_file = 'dummy.pdf'
# docx_file = 'converted.docx'

# cv = Converter(pdf_file)
# cv.convert(docx_file)
# cv.close()

import pdf2docx

# Set the path of the input PDF file
pdf_path = "dummy.pdf"

# Set the path of the output DOCX file
docx_path = "convert.docx"

# Convert the PDF file to DOCX format
pdf2docx.parse(pdf_path, docx_path)
