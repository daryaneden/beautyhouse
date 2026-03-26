import pytest_asyncio
from app.beauty_services.repository import BeautyServiceRepository
from app.beauty_services.service import BeautyServiceService
from app.settings import Settings 
from tests.fixtures.infrastructure import get_test_session


@pytest_asyncio.fixture()
async def beauty_services_service(get_test_session):
    return BeautyServiceService(beauty_service_repository=BeautyServiceRepository(db_session=get_test_session))

