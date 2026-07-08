import pytest_asyncio
import pytest
from app.presentation.dependencies import get_get_beauty_service_use_case
from tests.fakes.fake_beauty_service_data import FakeBeautyServiceData
from tests.fakes.fake_master_profile_data import FakeMasterProfileData
from app.presentation.beauty_services.v1.schemas import BeautyServiceSchema
from app.main import app as main_app
from app.application.beauty_services.use_cases.exceptions import ServiceNotFoundException

@pytest.mark.asyncio

class TestGetBeautyServiceRouter:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, get_beauty_service_use_case):

        main_app.dependency_overrides[get_get_beauty_service_use_case] = lambda: get_beauty_service_use_case
        
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

    async def test_get_beauty_service_success(self, client, setup_dependencies, fake_master, fake_beauty_service, auth_headers):

        data = {'beauty_service_id': 1}

        response = await client.get(url='/services/{service_id}', params=data, headers=auth_headers)

        beauty_service = response.json()

        assert response.status_code == 200
        assert BeautyServiceSchema.model_validate(beauty_service)
        assert beauty_service['master_id'] == 1
        assert beauty_service['service_name'] == 'test_service'

    async def test_get_beauty_service_not_found(self, client, setup_dependencies, fake_master, fake_beauty_service, auth_headers):

        data = {'beauty_service_id': 2}

        with pytest.raises(ServiceNotFoundException):
            await client.get(url='/services/{service_id}', params=data, headers=auth_headers)
