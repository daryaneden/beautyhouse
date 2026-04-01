from sqlalchemy import select, delete, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from beauty_services.models import BeautyServices
from infrastructure.database.accessor import get_db_session
from fastapi import Depends

class BeautyServiceRepository():
    def __init__(self, db_session: AsyncSession = Depends(get_db_session)):
        self.db_session = db_session

    async def get_beauty_services(self) -> list[BeautyServices]:
        services: list[BeautyServices] = (await self.db_session.execute(select(BeautyServices))).scalars().all()
        return services
    
    async def get_beauty_service(self, 
                                 service_id: int) -> BeautyServices | None:
        query = select(BeautyServices).where(BeautyServices.id == service_id)
        service: BeautyServices = (await self.db_session.execute(query)).scalar_one_or_none()
        return service
        
    async def get_master_beauty_service(self, 
                                 service_id: int,
                                 master_id: int) -> BeautyServices | None:
        query = select(BeautyServices).where(BeautyServices.id == service_id,
                                             BeautyServices.master_id == master_id)
        service: BeautyServices = (await self.db_session.execute(query)).scalar_one_or_none()
        return service

    async def create_beauty_service(self, 
                                 service_name: str, 
                                 client_name: str,
                                 master_id: int,
                                 date: str) -> int:
        query = insert(BeautyServices).values(service_name = service_name, 
                                              client_name = client_name,
                                              date = date,
                                              master_id = master_id).returning(BeautyServices.id)
        service_id: int = (await self.db_session.execute(query)).scalar_one_or_none()
        await self.db_session.commit()
        return service_id

    async def update_beauty_service_date(self, 
                                         service_id: int,
                                         date: str) -> BeautyServices:
        query = update(BeautyServices).where(BeautyServices.id == service_id).values(date = date).returning(BeautyServices.id)
        service_id: int = (await self.db_session.execute(query)).scalar_one_or_none()
        await self.db_session.commit()
        return await self.get_beauty_service(service_id)

    async def delete_beauty_service(self, service_id: int) -> None:
        query = delete(BeautyServices).where(BeautyServices.id == service_id)
        await self.db_session.execute(query)
        await self.db_session.commit()
                                    