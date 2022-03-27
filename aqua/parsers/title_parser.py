from datetime import datetime
from typing import Any

import pdfplumber

from aqua.schemas import TrialTitle


class TitleParser:

    def parse(self, doc: pdfplumber):
        page = doc.pages[:1]
        table = page[0].extract_tables({
            'edge_min_length': 15,  # this param get clean title table default 3
        })
        title = self._clean_title(table)
        return title

    def _clean_title(self, table: list[list[Any]]) -> TrialTitle:
        trial_title, trial_description = table

        trial_date = datetime.strptime(trial_description[2][1], '%d.%m.%Y %H:%M')

        return TrialTitle(
            measurement_object=trial_title[1][1],
            project=trial_description[0][1],
            report_date=trial_date,
            responsible_person=trial_description[3][1],
        )

