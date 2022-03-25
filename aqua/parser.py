import logging
from pathlib import Path
from typing import Any

import pdfplumber

from aqua import config
from aqua.schemas import Trials

trial = Path('aqua/reports/pdf_report.pdf')


def validator_toc_table(table: list[list[Any]], page_num: int) -> list[Trials]:
    new_table = []

    for row in table:
        if row[config.TOC['smd']] not in config.SMD_ERROR:
            new_row = Trials(
                smd=row[config.TOC['smd']],
                status=row[config.TOC['status']],
                value_description=row[config.TOC['value_description']],
                single_value=row[config.TOC['single_value']],
                trial_object=row[config.TOC['trial_object']],
            )
            new_table.append(new_row)

    return new_table


def table_printer(table: list[Trials]):
    for num, row in enumerate(table):
        smd = row.smd.replace('\n', ' ')
        row_num = num + 1
        control_string = f'{row_num}: smd = {smd}      status = {row.status} \n'
        logging.debug(control_string)


def toc_parser(start_page: int, finish_page: int) -> list[Trials]:
    doc = pdfplumber.open(trial)
    pages = doc.pages[start_page:finish_page]
    toc_list = []

    for page in pages:
        table = page.extract_table(config.toc_table_settings)
        valid_table = validator_toc_table(table, page.page_number)
        toc_list.extend(valid_table)

    return toc_list


def parse():
    toc_table = toc_parser(config.TOC_HEADING, config.TOC_BOTTOM)
    table_printer(toc_table)
