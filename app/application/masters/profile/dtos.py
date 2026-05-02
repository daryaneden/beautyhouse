from pydantic import BaseModel

class CreateMasterProfileDto(BaseModel):
    username: str | None = None
    full_name: str | None = None
    password: str | None = None
    email: str | None = None