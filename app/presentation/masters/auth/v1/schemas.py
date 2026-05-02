from pydantic import BaseModel

class MasterLoginSchema(BaseModel):
    username: str | None = None
    password: str | None = None

