from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.infrastructure.db import Base
import pytest_asyncio
from app.main import app as main_app
from app.infrastructure.db import get_db_session
from httpx import ASGITransport, AsyncClient
from typing import AsyncGenerator
import pytest

@pytest_asyncio.fixture(scope="function")
async def test_engine():
    engine = create_async_engine(
        url='postgresql+asyncpg://postgres:password@localhost:5432/beautyhouse-test', #5432 git
                             future=True,
                             echo=True,
                             pool_pre_ping=True
    )
    yield engine
    await engine.dispose()


@pytest_asyncio.fixture(scope='function')
async def test_session(test_engine):
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async_session = async_sessionmaker(
        test_engine,
                                            autoflush=False, 
                                            expire_on_commit=False
        )
    async with async_session() as session:
        yield session
        await session.rollback()
    

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
def app():
    return main_app

@pytest_asyncio.fixture(scope="function")
async def client(app, test_session) -> AsyncGenerator[AsyncClient, None]:
    async def _get_test_session():
        yield test_session

    app.dependency_overrides[get_db_session] = _get_test_session
    
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
          
    app.dependency_overrides.clear()

