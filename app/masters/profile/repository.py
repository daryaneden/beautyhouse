from sqlalchemy import select, delete, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.masters.profile.models import MasterProfile

class MasterProfileRepository():
    def __init__(self, db_session: AsyncSession):
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
        async with self.db_session as session:
            master_id: int = (await session.execute(query)).scalar()
            await session.commit()
            await session.flush()
            return await self.get_master(master_id)
        
    async def get_master(self,
                         master_id: int) -> MasterProfile | None:
        query = select(MasterProfile).where(MasterProfile.id == master_id)
        async with self.db_session as session:
            return (await session.execute(query)).scalar_one_or_none()
        
    async def get_master_by_username(self, username) -> MasterProfile:
        query = select(MasterProfile).where(MasterProfile.username == username)
        async with self.db_session as session:
            return (await session.execute(query)).scalar_one_or_none()