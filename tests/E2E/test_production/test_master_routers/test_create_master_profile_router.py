import pytest_asyncio
import pytest
from app.presentation.dependencies import get_create_master_profile_use_case
from httpx import AsyncClient
from app.main import app as main_app
from tests.fakes.fake_master_profile_data import FakeMasterProfileSchema

@pytest.mark.asyncio

class TestCreateMasterProfileRouter:
    
    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, create_master_profile_use_case):

        main_app.dependency_overrides[get_create_master_profile_use_case] = lambda: create_master_profile_use_case
        
        yield
        
        main_app.dependency_overrides.clear()

    async def test_create_master_profile_data(self, setup_dependencies):
        async with AsyncClient(app=main_app, base_url="http://test") as client:

            master_profile_data = FakeMasterProfileSchema()

            response = await client.post(url='/masters/', json = master_profile_data.model_dump())

            assert response.status_code == 200
            