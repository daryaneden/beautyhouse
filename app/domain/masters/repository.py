
#Здесь абстрактный класс репозитория, на который потом в infrastructure будут наложены методы sqlalchemy - ЧТО НУЖНО

from abc import ABC, abstractmethod
from app.domain.masters.model import MasterProfile

class MasterProfileRepository(ABC):

    @abstractmethod
    async def create_master_profile(self,
                                   username: str,
                                   full_name: str,
                                   password: str,
                                   email: str) -> MasterProfile:
        
        pass

    @abstractmethod
    async def get_master(self,
                         master_id: int) -> MasterProfile | None:
        
        pass

    @abstractmethod 
    async def get_master_by_username(self, 
                                     username: str) -> MasterProfile:
        
        pass