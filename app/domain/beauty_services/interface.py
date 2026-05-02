from abc import ABC, abstractmethod
from app.domain.beauty_services.entities import BeautyService

class BeautyServiceRepository(ABC):


    @abstractmethod
    async def get_beauty_service(self, 
                                 beauty_service_id: int) -> BeautyService | None:
        
        pass

    @abstractmethod
    async def get_beauty_services(self) -> list[BeautyService]:
        
        pass 

    @abstractmethod
    async def create_beauty_service(self, 
                                    beauty_service_create_data: BeautyService,
                                    master_id: int) -> None:
        
    
        pass
    
    @abstractmethod
    async def get_master_beauty_service(self, 
                                 beauty_service_id: int,
                                 master_id: int) -> BeautyService | None:
        
        pass

    @abstractmethod
    async def update_beauty_service_date(self, 
                                         beauty_service_update_data: BeautyService) -> None:
        
        pass
    
    @abstractmethod
    async def delete_beauty_service(self, beauty_service_id: int) -> None:

        pass

    