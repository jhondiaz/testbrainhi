

from typing import List, Optional
from pydantic import BaseModel


class HumanName(BaseModel):
    use: Optional[str] = "official"
    family: str
    given: List[str]