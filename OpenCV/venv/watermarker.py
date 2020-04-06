
import PyPDF2




#build a tool that takes in a watermark and watermarks every page

template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark =  PyPDF2.PdfFileReader(open('watermarker.pdf','rb')) # 'rb' read binary

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarker_out.pdf','wb') as file:
        output.write(file)