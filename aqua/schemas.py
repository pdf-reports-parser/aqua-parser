from typing import Optional

from pydantic import BaseModel


class Trials(BaseModel):
    smd: str
    status: Optional[str]
    single_value: Optional[str]
    trial_object: Optional[str]
