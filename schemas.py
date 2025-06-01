from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Literal

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[Literal["TODO", "IN_PROGRESS", "DONE"]] = "TODO"

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }