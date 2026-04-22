from abc import ABC, abstractmethod

class JwtProvider(ABC):

    @abstractmethod
    async def generate_access_token(self, master_id: int) -> str:

        pass

    @abstractmethod
    async def get_master_id_from_access_token(self, access_token: str) -> int:

        pass

    @abstractmethod
    async def get_request_master_id(token: str) -> int:

        pass