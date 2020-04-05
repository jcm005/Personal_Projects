import os
import sys
import PyPDF2

with open('Pdfs/original.pdf','rb') as my_pdf:

    reader = PyPDF2.PdfFileReader(my_pdf)
    page  = reader.getPage(0)
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as file:
        writer.write(file)




