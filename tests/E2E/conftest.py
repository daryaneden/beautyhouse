from app.presentation.jwt_service import JwtService
import pytest
from app.setting import Settings
from app.infrastructure.masters.repository import SQLAlchemyMastersRepository
from app.infrastructure.beauty_services.repository import SQLAlchemyBeautyServicesRepository
from app.application.masters.profile.use_cases.create_master_profile import CreateMasterProfileUseCase
from app.application.masters.auth.use_cases.master_login import MasterLoginUseCase
from app.application.beauty_services.use_cases.get_beauty_services import GetBeautyServicesUseCase
from app.application.beauty_services.use_cases.create_beauty_service import CreateBeautyServiceUsecase
from app.application.beauty_services.use_cases.update_beauty_service_date import UpdateBeautyServiceDateUsecase
from app.application.beauty_services.use_cases.delete_beauty_service import DeleteBeautyServicesUsecase
from app.application.beauty_services.use_cases.get_beauty_service import GetBeautyServiceUseCase

@pytest.fixture(scope='function')
def auth_headers():

    jwt_service = JwtService(settings=Settings())

    token = jwt_service.generate_access_token(master_id=1)
    
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture(scope='function')
def create_master_profile_use_case(test_session):
        return CreateMasterProfileUseCase(repo=SQLAlchemyMastersRepository(test_session))

@pytest.fixture(scope='function')
def master_login_use_case(test_session):
    return MasterLoginUseCase(repo=SQLAlchemyMastersRepository(test_session))

@pytest.fixture(scope='function')
def get_beauty_services_use_case(test_session):
    return GetBeautyServicesUseCase(repo=SQLAlchemyBeautyServicesRepository(test_session))

@pytest.fixture(scope='function')
def create_beauty_service_use_case(test_session):
    return CreateBeautyServiceUsecase(repo=SQLAlchemyBeautyServicesRepository(test_session))

@pytest.fixture(scope='function')
def update_beauty_service_use_case(test_session):
    return UpdateBeautyServiceDateUsecase(repo=SQLAlchemyBeautyServicesRepository(test_session))

@pytest.fixture(scope='function')
def delete_beauty_service_use_case(test_session):
    return DeleteBeautyServicesUsecase(repo=SQLAlchemyBeautyServicesRepository(test_session))

@pytest.fixture(scope='function')
def get_beauty_service_use_case(test_session):
    return GetBeautyServiceUseCase(repo=SQLAlchemyBeautyServicesRepository(test_session))
