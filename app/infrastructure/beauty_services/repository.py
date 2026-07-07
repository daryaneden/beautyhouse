from app.infrastructure.db import get_db_session
from app.infrastructure.beauty_services.models import BeautyService
from app.domain.beauty_services.interface import BeautyServiceRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update, insert

class SQLAlchemyBeautyServicesRepository(BeautyServiceRepository):

    def __init__(self, db_session: AsyncSession = get_db_session()):
        self.db_session = db_session

    async def get_beauty_services(self) -> list[BeautyService]:
        services: list[BeautyService] = (await self.db_session.execute(select(BeautyService))).scalars().all()
        return services
    
    async def get_beauty_service(self, 
                                 beauty_service_id: int) -> BeautyService | None:
        query = select(BeautyService).where(BeautyService.id == beauty_service_id)
        service: BeautyService = (await self.db_session.execute(query)).scalar_one_or_none()
        return service
        
    async def get_master_beauty_service(self, 
                                 beauty_service_id: int,
                                 master_id: int) -> BeautyService | None:
        query = select(BeautyService).where(BeautyService.id == beauty_service_id,
                                             BeautyService.master_id == master_id)
        service: BeautyService = (await self.db_session.execute(query)).scalar_one_or_none()
        return service

    async def create_beauty_service(self, 
                                 beauty_service_create_model: BeautyService,
                                 master_id: int) -> int:
        query = insert(BeautyService).values(service_name = beauty_service_create_model.service_name, 
                                              client_name = beauty_service_create_model.client_name,
                                              date = beauty_service_create_model.date,
                                              master_id = master_id).returning(BeautyService.id)
        service_id: int = (await self.db_session.execute(query)).scalar_one_or_none()
        return service_id

    async def update_beauty_service_date(self, 
                                         beauty_service_update_model: BeautyService) -> None:
        query = update(BeautyService).where(BeautyService.id == beauty_service_update_model.id).values(date = beauty_service_update_model.date).returning(BeautyService.id)
        await self.db_session.execute(query)

    async def delete_beauty_service(self, beauty_service_id: int) -> None:
        query = delete(BeautyService).where(BeautyService.id == beauty_service_id)
        await self.db_session.execute(query)

 
                 
