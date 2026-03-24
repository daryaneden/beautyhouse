import pytest_asyncio
import pytest
from app.beauty_services.repository import BeautyServiceRepository
from tests.fixtures.infrastructure import get_test_session

@pytest_asyncio.fixture(scope="session")
async def beauty_services_repository(get_test_session):
    yield BeautyServiceRepository(db_session=get_test_session) 
