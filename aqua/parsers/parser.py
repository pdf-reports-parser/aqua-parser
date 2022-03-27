import logging

import pdfplumber

from aqua.parsers import title_parser, toc_parser
from aqua.schemas import Trial, TrialTOC

logger = logging.getLogger(__name__)


class TrialParser:

    def __init__(self):
        self.title_parser = title_parser.TitleParser()
        self.toc_parser = toc_parser.TocParser()

    def parse(self, filename: str):
        doc = pdfplumber.open(filename)
        trial = Trial(
            title=self.title_parser.parse(doc),
            toc=self.toc_parser.parse(doc),
        )
        logger.info(trial.title)
        self.log_toc(trial.toc)
        return trial

    def log_toc(self, table: list[TrialTOC]):
        for num, row in enumerate(table):
            smd = row.smd.replace('\n', ' ')
            row_num = num + 1
            control_string = f'{row_num}: smd = {smd}; status = {row.status}'
            logger.info(control_string)
