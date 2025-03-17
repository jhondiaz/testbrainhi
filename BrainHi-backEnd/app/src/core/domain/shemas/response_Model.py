
from pydantic import BaseModel
from typing import Any, Optional

class ApiResponse(BaseModel):
    Codigo:Optional[int]=0
    Message: Optional[str]="Success"
    Value: Optional[Any] = None
    IsSuccess:Optional[ bool]=True