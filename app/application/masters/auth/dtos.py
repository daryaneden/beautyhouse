from pydantic import BaseModel

class MasterAuthDto(BaseModel):
    
    master_id: int | None = None
    access_token: str | None = None
