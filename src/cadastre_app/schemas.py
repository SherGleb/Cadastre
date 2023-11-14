from datetime import datetime
from pydantic import BaseModel


class QueryCrete(BaseModel):
    cadastral_number: str
    longitude: float
    latitude: float


