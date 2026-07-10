import pytest_asyncio
import pytest
from app.presentation.dependencies import get_delete_beauty_service_use_case
from tests.fakes.fake_beauty_service_data import FakeBeautyServiceData
from tests.fakes.fake_master_profile_data import FakeMasterProfileData
from app.main import app as main_app
from fastapi import status
from app.application.beauty_services.use_cases.exceptions import ServiceNotFoundException

@pytest.mark.asyncio

class TestDeleteBeautyServiceRouter:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, delete_beauty_service_use_case):

        main_app.dependency_overrides[get_delete_beauty_service_use_case] = lambda: delete_beauty_service_use_case
        
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

    async def test_delete_beauty_service_success(self, client, setup_dependencies, fake_master, fake_beauty_service, auth_headers):

        data = {'beauty_service_id': 1, 'master_id': 1}

        response = await client.delete(url='/services/{service_id}', params = data, headers=auth_headers)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    async def test_delete_beauty_service_not_found(self, client, setup_dependencies, fake_master, fake_beauty_service, auth_headers, mocker):
        
        data = {'beauty_service_id': 2, 'master_id': 1}

        with pytest.raises(ServiceNotFoundException):
            await client.delete(url='/services/{service_id}', params=data, headers=auth_headers)
