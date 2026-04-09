#Обычные классы, не зависящие от FastAPI, SQLAlchemy или Pydantic
from dataclasses import dataclass

@dataclass
class BeautyServices():
    
    id: int
    service_name: str
    client_name: str
    date: str
    master_id: int

