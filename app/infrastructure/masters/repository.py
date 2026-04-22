from app.infrastructure.db import get_db_session
from app.infrastructure.masters.models import MasterProfile
from app.domain.masters.interface import MasterProfileRepository
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

class SQLAlchemyMastersRepository(MasterProfileRepository):

    def __init__(self, db_session: AsyncSession = Depends(get_db_session)):
        self.db_session = db_session

    async def create_master_profile(self, 
                              username: str,
                              full_name: str,
                              password: str,
                              email: str) -> MasterProfile | None:
        query = insert(MasterProfile).values(username=username,
                                       full_name=full_name,
                                       password=password,
                                       email=email).returning(MasterProfile.id)
        master_id: int = (await self.db_session.execute(query)).scalar()
        await self.db_session.commit()
        await self.db_session.flush()
        return await self.get_master(master_id)
        
    async def get_master(self,
                         master_id: int) -> MasterProfile | None:
        query = select(MasterProfile).where(MasterProfile.id == master_id)
        return (await self.db_session.execute(query)).scalar_one_or_none()
        
    async def get_master_by_username(self, username) -> MasterProfile:
        query = select(MasterProfile).where(MasterProfile.username == username)
        return (await self.db_session.execute(query)).scalar_one_or_none()