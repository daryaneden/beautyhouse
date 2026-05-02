import pytest_asyncio
from app.infrastructure.beauty_services.repository import SQLAlchemyBeautyServicesRepository

@pytest_asyncio.fixture(scope="session")
async def beauty_services_repository(get_test_session):
    yield SQLAlchemyBeautyServicesRepository(db_session=get_test_session) 
 