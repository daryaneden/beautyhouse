import pytest_asyncio
import pytest
from app.presentation.dependencies import get_update_beauty_service_date_use_case
from tests.fakes.fake_beauty_service_data import FakeBeautyServiceUpdateSchema, FakeBeautyServiceData
from tests.fakes.fake_master_profile_data import FakeMasterProfileData
from app.main import app as main_app
from app.application.beauty_services.use_cases.exceptions import ServiceNotFoundException

@pytest.mark.asyncio

class TestUpdateBeautyServiceDateRouter:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, update_beauty_service_use_case):

        main_app.dependency_overrides[get_update_beauty_service_date_use_case] = lambda: update_beauty_service_use_case
        
        yield
        
        main_app.dependency_overrides.clear()

    @pytest_asyncio.fixture(scope='function')
    async def fake_master(self, test_session):

        master = FakeMasterProfileData()
        
        test_session.add(master)
        await test_session.commit()
     
        return master
    
    @pytest_asyncio.fixture(scope='function')
    async def fake_beauty_service(self, test_session):

        beauty_service = FakeBeautyServiceData()
        
        test_session.add(beauty_service)
        await test_session.commit()
     
        return beauty_service

    async def test_update_beauty_service_date_success(self, client, setup_dependencies, fake_master, fake_beauty_service, auth_headers):

        beauty_service_update_schema = FakeBeautyServiceUpdateSchema()

        response = await client.patch(url='/services/{service_id}', json = beauty_service_update_schema.model_dump(), headers=auth_headers)
        beauty_service = response.json()

        assert response.status_code == 200
        assert beauty_service['id'] == beauty_service_update_schema.id
        assert beauty_service['date'] == beauty_service_update_schema.date

    async def test_update_beauty_service_not_found(self, client, setup_dependencies, fake_master, fake_beauty_service, auth_headers):
        
        beauty_service_update_schema = FakeBeautyServiceUpdateSchema()
        beauty_service_update_schema.id = 2

        with pytest.raises(ServiceNotFoundException):
            await client.patch(url='/services/{service_id}', json = beauty_service_update_schema.model_dump(), headers=auth_headers)
