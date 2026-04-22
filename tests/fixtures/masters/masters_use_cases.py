import pytest_asyncio
from app.application.masters.auth.use_cases import MasterAuthUseCases
from app.application.masters.profile.use_cases import MasterProfileUseCases
from app.infrastructure.masters.repository import SQLAlchemyMastersRepository
from app.setting import Settings 

@pytest_asyncio.fixture()
async def master_auth_use_cases(get_test_session):
    return MasterAuthUseCases(master_profile_repository=SQLAlchemyMastersRepository(db_session=get_test_session),
                             settings=Settings())

@pytest_asyncio.fixture(scope='session')
async def master_profile_use_cases(get_test_session):
    return MasterProfileUseCases(master_profile_repository=SQLAlchemyMastersRepository(db_session=get_test_session),
                                master_auth_service=MasterAuthUseCases(master_profile_repository=SQLAlchemyMastersRepository(db_session=get_test_session), 
                                                                       settings=Settings()  
                                ))
