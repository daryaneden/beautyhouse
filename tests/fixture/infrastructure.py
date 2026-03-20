from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.settings import Settings
from app.infrastructure.database.database import Base
from app.settings import Settings
import pytest_asyncio
import pytest


@pytest.fixture
def settings():
    return Settings()

test_engine = create_async_engine(url='postgresql+asyncpg://postgres:password@localhost:5435/beautyhouse-test',
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
        

@pytest_asyncio.fixture(scope="session")
async def get_test_session():
    yield AsyncSessionFactory()