from pydantic import BaseModel


class Trials(BaseModel):
    smd: str
    status: str
    single_value: str
    trial_object: str
