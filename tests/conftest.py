from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.domain.masters.interface import MasterProfileRepository
from app.domain.beauty_services.interface import BeautyServiceRepository
from app.infrastructure.masters.models import MasterProfile
from app.infrastructure.beauty_services.models import BeautyService
from app.infrastructure.db import Base
import pytest_asyncio
import pytest

test_engine = create_async_engine(url='postgresql+asyncpg://postgres:password@localhost:5435/beautyhouse-test', #5432 git
                             future=True,
                             echo=True,
                             pool_pre_ping=True)

AsyncSessionFactory = async_sessionmaker(test_engine,
                                         autoflush=False,
                                         expire_on_commit=False)

@pytest_asyncio.fixture(scope="session", autouse=True)
async def init_models():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield test_engine
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture(scope="function")
async def get_test_session():
    async with AsyncSessionFactory() as session:
        async with session.begin():
            yield session
            await session.rollback()  #?
