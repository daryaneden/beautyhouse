import pytest_asyncio
from app.application.masters.auth.use_cases import MasterAuthUseCases
from app.application.masters.profile.use_cases import MasterProfileUseCases
from app.infrastructure.masters.repository import SQLAlchemyMastersRepository
from app.infrastructure.jwt_service import JwtService
from app.setting import Settings 

@pytest_asyncio.fixture()
async def master_auth_use_cases(get_test_session):
    return MasterAuthUseCases(repo=SQLAlchemyMastersRepository(db_session=get_test_session),
                             jwt_provider=JwtService())

@pytest_asyncio.fixture(scope='session')
async def master_profile_use_cases(get_test_session):
    return MasterProfileUseCases(repo=SQLAlchemyMastersRepository(db_session=get_test_session),
                                jwt_provider=JwtService()  
                                )
