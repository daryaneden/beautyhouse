#Здесь описывается бизнес-логика(как в сервисном слое - РЕАЛИЗАЦИЯ)
#Сценарии, заложенные в приложении
#принимает entities и возвращает dtos

from app.domain.beauty_services.interface import BeautyServicesRepository
from app.domain.beauty_services.model import BeautyServices
from app.application.beauty_services.dtos import BeautyServiceDto
from app.application.beauty_services.exceptions import ServiceNotFoundException


class BeautyServicesUsecases:

    def __init__(self, repo: BeautyServicesRepository):

        self.repo = repo

    async def get_beauty_services(self) -> list[BeautyServiceDto]:

        services: BeautyServices = await self.repo.get_beauty_services()
        services_dto = [BeautyServiceDto.model_validate(service) for service in services]
        return services_dto
    
    async def create_beauty_service(self, 
                                    service_name: str, 
                                    client_name: str,
                                    master_id: int,
                                    date: str) -> BeautyServiceDto | None:
        
        service_id: int = await self.repo.create_beauty_service(service_name = service_name, 
                                                                                client_name = client_name,
                                                                                date = date,
                                                                                master_id = master_id)
        
        service = await self.repo.get_beauty_service(service_id=service_id)
        return BeautyServiceDto.model_validate(service)
    
    async def update_beauty_service_date(self, 
                                         service_id: int,
                                         date: str,
                                         master_id: int) -> BeautyServiceDto:
        service = await self.repo.get_master_beauty_service(service_id=service_id,
                                                                          master_id=master_id)
        if not service:
            raise ServiceNotFoundException
        service = await self.repo.update_beauty_service_date(service_id=service_id,
                                                                                  date=date)
        return BeautyServiceDto.model_validate(service)
    
    async def delete_beauty_service(self, service_id: int, master_id: int) -> None:
        service = await self.repo.get_master_beauty_service(service_id=service_id,
                                                                                 master_id=master_id)
        if not service:
            raise ServiceNotFoundException
        await self.repo.delete_beauty_service(service_id=service_id)