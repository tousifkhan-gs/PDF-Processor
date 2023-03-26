import PyPDF2, sys

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

inputs = sys.argv[1:]        
pdf_merger(inputs)
 
print("All Done!")
