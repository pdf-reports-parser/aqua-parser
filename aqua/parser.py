from pathlib import Path
from typing import Any

import pdfplumber

from aqua.schemas import Trials

trial = Path('aqua/reports/pdf_report.pdf')


def table_validator(table: list[list[Any]]):
    new_table = []
    for row in table:
        if row[0] is not None:
            new_row = Trials(
                smd=row[0],
                status=row[1],
                single_value=row[4],
                trial_object=row[8],
            )
            new_table.append(new_row)
    return new_table


def plumber_parse():
    doc = pdfplumber.open(trial)
    page = doc.pages[1]
    table = page.extract_table()
    valid_table = table_validator(table)
    for row in valid_table:
        print(row)


def parse():
    plumber_parse()
