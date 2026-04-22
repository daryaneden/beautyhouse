from pydantic import BaseModel

class BeautyServiceSchema(BaseModel):
    id: int | None = None
    service_name: str | None = None
    client_name: str | None = None
    date: str | None = None
    master_id: int

    class Config:
        from_attributes = True

class BeautyServiceCreateSchema(BaseModel):
    service_name: str | None = None
    client_name: str | None = None
    date: str | None = None