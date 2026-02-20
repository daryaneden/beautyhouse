from pydantic import BaseModel

class MyClients(BaseModel):
    id: int
    name: str
    next_visit: str
    visits_number: int
    discount: int | None

    class Config:
        from_attributes = True