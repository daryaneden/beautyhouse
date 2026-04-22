from pydantic import BaseModel

class MasterAuthRequestSchema(BaseModel):
    username: str | None = None
    password: str | None = None

