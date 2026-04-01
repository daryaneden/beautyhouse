import pytest_asyncio
from masters.profile.repository import MasterProfileRepository



@pytest_asyncio.fixture()
def master_profile_repository(get_test_session):
    return MasterProfileRepository(db_session=get_test_session) 