from pathlib import Path
from typing import Any

import pdfplumber

from aqua import config
from aqua.schemas import Trials

trial = Path('aqua/reports/pdf_report.pdf')


def table_validator(table: list[list[Any]], page_num: int):
    new_table = []
    if page_num == config.HEADING_TOC:
        rule = config.TOC['heading']
    else:
        rule = config.TOC['content']
    for row in table:
        if row[rule['smd']] not in config.SMD_ERROR:
            new_row = Trials(
                smd=row[rule['smd']],
                status=row[rule['status']],
                single_value=row[rule['single_value']],
                trial_object=row[rule['trial_object']],
            )
            new_table.append(new_row)
    return new_table


def table_handler(table):
    for row in table:
        print(row)


def plumber_parse():
    doc = pdfplumber.open(trial)
    pages = doc.pages[1:4]
    for page in pages:
        table = page.extract_table()
        valid_table = table_validator(table, page.page_number)
        table_handler(valid_table)


def parse():
    plumber_parse()
