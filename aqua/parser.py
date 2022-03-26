import logging
from typing import Any

import pdfplumber

from aqua.schemas import Trials

logger = logging.getLogger(__name__)

SMD_ERROR = ('SMD', None, '')


class TocParser:

    def parse(self, filename: str, start: int = 2, finish: int = 3):
        toc = self._get_toc(
            filename=filename,
            start_page=start,
            finish_page=finish,
        )

        self._print_toc(toc)

    def _clean_toc(self, table: list[list[Any]]) -> list[Trials]:
        new_table = []

        for row in table:
            smd, status, description, value, obj = row
            if smd in SMD_ERROR:
                continue

            trial = Trials(
                smd=smd,
                status=status,
                value_description=description,
                single_value=value,
                trial_object=obj,
            )
            new_table.append(trial)

        return new_table

    def _get_toc(self, filename: str, start_page: int, finish_page: int) -> list[Trials]:
        doc = pdfplumber.open(filename)
        pages = doc.pages[start_page:finish_page]
        toc_list = []

        for page in pages:
            table = page.extract_table({
                'edge_min_length': 200,  # this param get clean toc table default 3
            })

            valid_table = self._clean_toc(table)
            toc_list.extend(valid_table)

        return toc_list

    def _print_toc(self, table: list[Trials]):
        for num, row in enumerate(table):
            smd = row.smd.replace('\n', ' ')
            row_num = num + 1
            control_string = f'{row_num}: smd = {smd}      status = {row.status} \n'
            logger.info(control_string)
