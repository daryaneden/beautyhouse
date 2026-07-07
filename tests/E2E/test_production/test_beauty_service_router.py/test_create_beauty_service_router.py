import pytest_asyncio
import pytest
from app.presentation.dependencies import get_create_beauty_service_use_case
from tests.fakes.fake_beauty_service_data import FakeBeautyServiceCreateSchema
from tests.fakes.fake_master_profile_data import FakeMasterProfileData
from app.main import app as main_app

@pytest.mark.asyncio

class TestCreateBeautyServiceRouter:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, create_beauty_service_use_case):

        main_app.dependency_overrides[get_create_beauty_service_use_case] = lambda: create_beauty_service_use_case
        
        yield
        
        main_app.dependency_overrides.clear()

    @pytest_asyncio.fixture(scope='function')
    async def fake_master(self, test_session):

        master = FakeMasterProfileData()
        
        test_session.add(master)
        await test_session.commit()
     
        return master

    async def test_create_beauty_service(self, client, setup_dependencies, fake_master, auth_headers):

        beauty_service_create_schema = FakeBeautyServiceCreateSchema()

        response = await client.post(url='/services/', json = beauty_service_create_schema.model_dump(), headers=auth_headers)

        beauty_service = response.json()

        assert response.status_code == 200

        assert beauty_service['id'] == 1
