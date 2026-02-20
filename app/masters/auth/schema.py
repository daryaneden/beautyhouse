from pydantic import BaseModel

class MasterLoginSchema(BaseModel):
    master_id: int | None = None
    access_token: str | None = None
