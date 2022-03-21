import logging
from io import StringIO
from itertools import islice
from pathlib import Path

import tabula
from pdfminer.converter import TextConverter
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import pdfplumber

output_string = StringIO()
trial = Path('aqua/reports/pdf_report.pdf')


def miner_parse():
    output_string = StringIO()
    with open(trial, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        pages = PDFPage.create_pages(doc)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        file_pages = list(islice(pages, 1))
        for page in file_pages:
            interpreter.process_page(page)
            #print(output_string.read())


    export_text = output_string.getvalue()
    print(export_text, type(export_text))
    write_text(export_text)



def write_text(text: str):
    with open(Path('aqua/reports/export.txt'), 'w', encoding='utf-8') as file:
        file.write(text)


def tabula_parse():
    table = tabula.read_pdf(trial, pages=2)
    print(table[0])

def plumber_parse():
    doc = pdfplumber.open(trial)
    page = doc.pages[1]
    table = page.extract_table()
    import json
    #print(json.dumps(table, indent=4))
    print(table)

def parse():
    #miner_parse()
    #tabula_parse()
    plumber_parse()
