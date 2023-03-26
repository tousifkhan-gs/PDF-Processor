import PyPDF2

with open ('pdf-text.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Create a PDF writer object
    writer = PyPDF2.PdfWriter()
    
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        page.rotate(180)
        writer.add_page(page)
        

with open('rotate.pdf', 'wb') as new_file:
    writer.write(new_file)
    
    