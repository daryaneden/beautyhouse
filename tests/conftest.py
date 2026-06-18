from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.domain.masters.interface import MasterProfileRepository
from app.domain.beauty_services.interface import BeautyServiceRepository
from app.infrastructure.db import Base
import pytest_asyncio
import pytest
from unittest.mock import MagicMock

# test_engine = create_async_engine(url='postgresql+asyncpg://postgres:password@localhost:5432/beautyhouse-test', 
#                              future=True,
#                              echo=True,
#                              pool_pre_ping=True)

# AsyncSessionFactory = async_sessionmaker(test_engine,
#                                          autoflush=False,
#                                          expire_on_commit=False)

# @pytest_asyncio.fixture(scope="session", autouse=True)
# async def init_models():
#     async with test_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     yield test_engine
#     async with test_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)

# @pytest_asyncio.fixture(scope="session")
# async def get_test_session():
#     async with AsyncSessionFactory() as session:
#         async with session.begin():
#             yield session
            #session.rollback()?

# @pytest.fixture
# def mock_user_repo():
#     return MagicMock(spec=MasterProfileRepository)

# @pytest.fixture
# def mock_beauty_services_repo():
#     return MagicMock(spec=BeautyServiceRepository)