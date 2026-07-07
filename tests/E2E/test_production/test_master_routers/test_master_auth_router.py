import pytest_asyncio
import pytest
from app.presentation.dependencies import get_master_login_use_case
from tests.fakes.fake_master_auth_data import FakeMasterLoginSchema
from tests.fakes.fake_master_profile_data import FakeMasterProfileData
from app.application.masters.auth.use_cases.exceptions import MasterNotFoundException, IncorrectPasswordException
from app.main import app as main_app

@pytest.mark.asyncio

class TestMasterAuthRouter:

    @pytest_asyncio.fixture(scope='function')
    async def setup_dependencies(self, master_login_use_case):

        main_app.dependency_overrides[get_master_login_use_case] = lambda: master_login_use_case
        
        yield
        
        main_app.dependency_overrides.clear()

    @pytest_asyncio.fixture(scope='function')
    async def fake_master(self, test_session):

        master = FakeMasterProfileData()
        
        test_session.add(master)
        await test_session.commit()
     
        return master

    async def test_master_login_success(self, client, fake_master, setup_dependencies):

        master_login_data = FakeMasterLoginSchema()

        response = await client.post(url='/masters/auth/', json=master_login_data.model_dump())

        assert response.status_code == 200

    async def test_master_login_not_found(self, client, fake_master, setup_dependencies):
        master_login_data = FakeMasterLoginSchema()
        master_login_data.username = 'ghost_master'

        with pytest.raises(MasterNotFoundException):
            await client.post(url='/masters/auth/', json=master_login_data.model_dump())

    async def test_master_login_incorrect_password(self, client, fake_master, setup_dependencies):
        master_login_data = FakeMasterLoginSchema()
        master_login_data.password = 'incorrect_password'

        with pytest.raises(IncorrectPasswordException):
            await client.post(url='/masters/auth/', json=master_login_data.model_dump())
