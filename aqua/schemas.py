from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TrialTitle(BaseModel):
    measurement_object: str
    project: str
    report_date: datetime
    responsible_person: str


class Trials(BaseModel):
    smd: str
    status: Optional[str]
    value_description: Optional[str]
    single_value: Optional[str]
    trial_object: Optional[str]
