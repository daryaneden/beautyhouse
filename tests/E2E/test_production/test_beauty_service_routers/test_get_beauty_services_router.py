import pytest_asyncio
import pytest
from app.presentation.dependencies import get_get_beauty_services_use_case
from tests.fakes.fake_beauty_service_data import FakeBeautyServiceData
from tests.fakes.fake_master_profile_data import FakeMasterProfileData
from app.presentation.beauty_services.v1.schemas import BeautyServiceSchema
from app.main import app as main_app

@pytest.mark.asyncio

class TestGetBeautyServicesRouter:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, get_beauty_services_use_case):

        main_app.dependency_overrides[get_get_beauty_services_use_case] = lambda: get_beauty_services_use_case
        
        yield
        
        main_app.dependency_overrides.clear()

    @pytest_asyncio.fixture(scope='function')
    async def fake_master(self, test_session):

        master = FakeMasterProfileData()
        
        test_session.add(master)
        await test_session.commit()


    @pytest_asyncio.fixture(scope='function')
    async def fake_beauty_service(self, test_session):

        beauty_service = FakeBeautyServiceData()
        
        test_session.add(beauty_service)
        await test_session.commit()
     
        return beauty_service

    async def test_get_beauty_services(self, client, setup_dependencies, fake_master, fake_beauty_service, auth_headers):

        response = await client.get(url='/services/all', headers=auth_headers)

        beauty_services = response.json()

        assert response.status_code == 200

        assert isinstance(beauty_services, list)
        assert BeautyServiceSchema.model_validate(beauty_services[0])
        assert len(beauty_services) == 1
