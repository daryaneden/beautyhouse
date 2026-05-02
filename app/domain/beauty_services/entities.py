from dataclasses import dataclass

@dataclass
class BeautyService():
    
    id: int
    service_name: str
    client_name: str
    date: str
    master_id: int

