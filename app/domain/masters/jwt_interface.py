from abc import ABC, abstractmethod
from app.domain.masters.model import MasterProfile

class JwtProvider(ABC):

    @abstractmethod
    async def generate_access_token(self, master_id: int) -> str:

        pass

    @abstractmethod
    async def get_master_id_from_access_token(self, access_token: str) -> int:

        pass