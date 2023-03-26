import PyPDF2, sys

if len(sys.argv) < 3:
    print("Usage: python python_script_name.py watermark.pdf file1.pdf [file2.pdf file3.pdf...]")
    sys.exit(1)

watermark = PyPDF2.PdfReader(open(sys.argv[1], 'rb'))

for file in sys.argv[2:]:
    pdf_file = PyPDF2.PdfReader(open(f'{file}', 'rb'))
    output = PyPDF2.PdfWriter()
    
    for page in range(len(pdf_file.pages)):
        single_page = pdf_file.pages[page]
        single_page.merge_page(watermark.pages[0])
        output.add_page(single_page)
            
        with open(f"watermarked_{file}", "wb") as new_file:
            output.write(new_file)
        print(f"watermarked: {file}")



'''
    Single File PDF Watermark Script
'''
# template = PyPDF2.PdfReader(open('dummy.pdf', 'rb'))
# watermark = PyPDF2.PdfReader(open('213_wtr.pdf', 'rb'))
# output = PyPDF2.PdfWriter()

# for i in range(len(template.pages)):
#     page = template.pages[i]
#     page.merge_page(watermark.pages[0])
#     output.add_page(page)
    
#     with open('watermarked-pdf.pdf', 'wb') as file:
#         output.write(file)