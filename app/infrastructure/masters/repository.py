from app.infrastructure.db import get_db_session
from app.infrastructure.masters.models import MasterProfile
from app.domain.masters.interface import MasterProfileRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

class SQLAlchemyMastersRepository(MasterProfileRepository):

    def __init__(self, db_session: AsyncSession = get_db_session()):
        self.db_session = db_session

    async def create_master_profile(self, 
                              master_profile_create_model: MasterProfile) -> int:
        query = insert(MasterProfile).values(username=master_profile_create_model.username,
                                       full_name=master_profile_create_model.full_name,
                                       password=master_profile_create_model.password,
                                       email=master_profile_create_model.email).returning(MasterProfile.id)
        master_id = (await self.db_session.execute(query)).scalar()
        return master_id
        
    async def get_master(self,
                         master_id: int) -> MasterProfile | None:
        query = select(MasterProfile).where(MasterProfile.id == master_id)
        return (await self.db_session.execute(query)).scalar_one_or_none()
        
    async def get_master_by_username(self, username) -> MasterProfile:
        query = select(MasterProfile).where(MasterProfile.username == username)
        return (await self.db_session.execute(query)).scalar_one_or_none()