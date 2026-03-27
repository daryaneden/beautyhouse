import pytest_asyncio
from app.masters.auth.service import MasterAuthService
from app.masters.profile.service import MasterProfileService
from app.masters.profile.repository import MasterProfileRepository
from app.settings import Settings 

@pytest_asyncio.fixture()
async def master_auth_service(get_test_session):
    return MasterAuthService(master_profile_repository=MasterProfileRepository(db_session=get_test_session),
                             settings=Settings())

@pytest_asyncio.fixture(scope='session')
async def master_profile_service(get_test_session):
    return MasterProfileService(master_profile_repository=MasterProfileRepository(db_session=get_test_session),
                                master_auth_service=MasterAuthService(master_profile_repository=MasterProfileRepository(db_session=get_test_session), 
                                                                       settings=Settings()  
                                ))

# @pytest_asyncio.fixture
# # async def master_profile_repository():
# #     return MasterProfileRepository(db_session=get_test_session)