import pytest_asyncio
from app.infrastructure.beauty_services.repository import SQLAlchemyBeautyServicesRepository
from app.application.beauty_services.use_cases import BeautyServicesUsecases


@pytest_asyncio.fixture()
async def beauty_services_use_cases(get_test_session):
    return BeautyServicesUsecases(repo=SQLAlchemyBeautyServicesRepository(db_session=get_test_session))

