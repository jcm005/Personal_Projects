import sys
import PyPDF2

#combine two pdf's to form one pdf

inputs = sys.argv[1:]


def merging(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    merger.write('super.pdf')



merging(inputs)