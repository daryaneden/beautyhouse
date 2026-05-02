from dataclasses import dataclass

@dataclass
class MasterProfile():
    
    id: int | None
    username: str
    full_name: str
    password: str
    email: str

