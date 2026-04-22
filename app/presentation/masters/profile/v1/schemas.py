from pydantic import BaseModel

class MasterProfileRequestSchema(BaseModel):
    username: str | None = None
    full_name: str | None = None
    password: str | None = None
    email: str | None = None

class MasterProfileResponseSchema(BaseModel):
    master_id: int | None = None
    access_token: str | None = None