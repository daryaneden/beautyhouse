from sqlalchemy import select, delete, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from app.beauty_services.schema import BeautyServiceCreateSchema, BeautyServiceSchema
from app.beauty_services.models import BeautyServices

class BeautyServiceRepository():
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_beauty_services(self) -> list[BeautyServices]:
        async with self.db_session as session:
            services: list[BeautyServices] = (await session.execute(select(BeautyServices))).scalars().all()
        return services
    
    async def get_beauty_service(self, 
                                 service_id: int) -> BeautyServices | None:
        query = select(BeautyServices).where(BeautyServices.id == service_id)
        with self.db_session as session:
            service: BeautyServices = (await session.execute(query).scalar_one_or_none())
            return service
        
    async def get_master_beauty_service(self, 
                                 service_id: int,
                                 master_id: int) -> BeautyServices | None:
        query = select(BeautyServices).where(BeautyServices.id == service_id,
                                             BeautyServices.master_id == master_id)
        with self.db_session as session:
            service: BeautyServices = (await session.execute(query).scalar_one_or_none())
            return service

    async def create_beauty_service(self, 
                                 service: BeautyServiceCreateSchema, 
                                 master_id: int) -> int:
        query = insert(BeautyServices).values(name = service.service_name, 
                                              client_name = service.client_name,
                                              date = service.date,
                                              master_id = master_id).returning(BeautyServices.id)
        with self.db_session as session:
            service_id: int = (await session.execute(query).scalar_one_or_none())
            await session.commit()
            return service_id

    async def update_beauty_service_date(self, 
                                         service_id: int,
                                         date: str) -> BeautyServices:
        query = update(BeautyServices).where(BeautyServices.id == service_id).values(date = date)
        with self.db_session as session:
            service_id: int = (await session.execute(query).scalars())
            await session.commit()
            return self.get_beauty_service(service_id)

    async def delete_beauty_service(self, service_id: int) -> None:
        query = delete(BeautyServices).where(BeautyServices.id == service_id)
        with self.db_session as session:
            service_id: int = await session.execute(query)
            await session.commit()
                                    