#Здесь абстрактный класс репозитория, на который потом в infrastructure будут наложены методы sqlalchemy
# классы в infrastructure будут наследоваться от этих классов


from abc import ABC, abstractmethod
from app.domain.beauty_services.entities import BeautyServices

class BeautyServicesRepository(ABC):


    @abstractmethod
    async def get_beauty_service(self, 
                                 service_id: int) -> BeautyServices | None:
        
        pass

    @abstractmethod
    async def get_beauty_services(self) -> list[BeautyServices]:
        
        pass 

    @abstractmethod
    async def create_beauty_service(self, 
                                    service_name: str, 
                                    client_name: str,
                                    master_id: int,
                                    date: str) -> BeautyServices:
        
    
        pass
    
    @abstractmethod
    async def get_master_beauty_service(self, 
                                 service_id: int,
                                 master_id: int) -> BeautyServices | None:
        
        pass

    @abstractmethod
    async def update_beauty_service_date(self, 
                                         service_id: int,
                                         date: str,
                                         master_id: int) -> BeautyServices:
        
        pass
    
    @abstractmethod
    async def delete_beauty_service(self, service_id: int, 
                                    master_id: int) -> None:

        pass

    