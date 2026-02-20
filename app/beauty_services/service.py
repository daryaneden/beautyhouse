from app.beauty_services.repository import BeautyServiceRepository
from app.beauty_services.schema import BeautyServiceSchema, BeautyServiceCreateSchema
from app.exceptions import ServiceNotFound

class BeautyServiceService:
    beauty_service_repository: BeautyServiceRepository

    async def get_beauty_services(self) -> list[BeautyServiceSchema]:
        services = await self.beauty_service_repository.get_beauty_services()
        services_schema = [BeautyServiceSchema.model_validate(service) for service in services]
        return services_schema
    
    async def create_beauty_service(self, 
                                    body: BeautyServiceCreateSchema,
                                 master_id: int) -> BeautyServiceSchema | None:
        service_id = await self.beauty_service_repository.create_beauty_service(service=body, master_id=master_id)
        service = await self.beauty_service_repository.get_beauty_service(service_id=service_id)
        return service.model_validate()
    
    async def update_beauty_service_date(self, 
                                         service_id: int,
                                         date: str,
                                         master_id: int) -> BeautyServiceSchema:
        service = await self.beauty_service_repository.get_master_beauty_service(service_id=service_id,
                                                                          master_id=master_id)
        if not service:
            raise ServiceNotFound
        service = await self.beauty_service_repository.update_beauty_service_date(service_id=service_id,
                                                                                  date=date)
        return service.model_validate()
    
    async def delete_beauty_service(self, service_id: int, master_id: int) -> None:
        service = await self.beauty_service_repository.get_master_beauty_service(service_id=service_id,
                                                                                 master_id=master_id)
        if not service:
            raise ServiceNotFound
        await self.beauty_service_repository.delete_beauty_service(service_id=service_id)

        
