from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ExampleSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    type: str
    col_1: str
    col_2: str | None = None
    active: bool
