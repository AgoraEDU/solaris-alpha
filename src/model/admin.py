"""
file: admin.py
authors:
    - Muhammad Bilal Khan <@Hi-kue>
date: 2024-10-13
description:
    - Overall structure and model for users who have admin privileges.
notes:
    - This model is very similar to the client model, but with some differences.
"""


import uuid

from pydantic import BaseModel
from datetime import datetime

generate_uuid = lambda: uuid.uuid4().int & (1 << 64) - 1


class Admin(BaseModel):
    id: int = None
    name: str
    password: str
    email: str
    is_active: bool = False
    is_superuser: bool = True
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True
        orm_mode = True
        extra = "allow"

    def __post_init__(self):
        if self.id is None:
            self.id = generate_uuid()
