"""
file: client.py
authors:
    - Muhammad Bilal Khan <@Hi-kue>
date: 2024-10-13
description:
    - Overall structure and model for clients who need to have their information stored.
notes:
    - Kwargs is considered as a dictionary, which can only contain JSON-serializable data.
    - This means that we will need to use the JSON data type for kwargs in MySQL.
"""

from pydantic import BaseModel, BaseConfig
from datetime import datetime
import uuid

generate_uuid = lambda: uuid.uuid4().int & (1 << 64) - 1


class Client(BaseModel):
    id: int = None
    email: str
    kwargs: dict = {}
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
