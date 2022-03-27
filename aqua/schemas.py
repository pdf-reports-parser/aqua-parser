from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TrialTitle:
    measurement_object: str
    project: str
    report_date: datetime
    responsible_person: str


@dataclass
class TrialTOC:
    smd: str
    status: Optional[str]
    value_description: Optional[str]
    single_value: Optional[str]
    trial_object: Optional[str]


@dataclass
class Trial:
    title: TrialTitle
    toc: list[TrialTOC]
