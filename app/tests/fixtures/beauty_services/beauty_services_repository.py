import pytest_asyncio
from beauty_services.repository import BeautyServiceRepository

@pytest_asyncio.fixture(scope="session")
async def beauty_services_repository(get_test_session):
    yield BeautyServiceRepository(db_session=get_test_session) 
