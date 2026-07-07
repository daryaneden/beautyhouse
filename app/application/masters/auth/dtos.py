from pydantic import BaseModel

class MasterAuthDto(BaseModel):
    
    master_id: int | None = None
    access_token: str | None = None

class MasterLoginDataDto(BaseModel):

    username: str | None = None
    password: str | None = None
