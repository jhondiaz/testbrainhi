
from pydantic import BaseModel
from typing import Any, Optional

class RepoResponse(BaseModel):
    Message: Optional[str]="Success"
    Value: Optional[Any] = None
    IsSuccess:Optional[ bool]=True