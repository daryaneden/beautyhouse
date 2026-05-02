import pytest_asyncio
from app.infrastructure.masters.repository import SQLAlchemyMastersRepository



@pytest_asyncio.fixture()
def master_profile_repository(get_test_session):
    return SQLAlchemyMastersRepository(db_session=get_test_session) 