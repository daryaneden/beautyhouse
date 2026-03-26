import pytest
from tests.fixtures.infrastructure import get_test_session

pytestmark = pytest.mark.asyncio

@pytest.mark.asyncio(loop_scope="session")
async def test_create_master_profile(master_profile_service):
    username = 'test_username_1'
    full_name = 'test_full_name'
    password = 'test_password'
    email = 'test_email'

    master_id = await master_profile_service.create_master_profile(username=username, 
                                                                   full_name=full_name, 
                                                                   password=password, 
                                                                   email=email)

    assert master_id is not None

@pytest.mark.asyncio(loop_scope="session")
async def test_login(master_auth_service):
    username = 'test_username_1'
    password = 'test_password'
    
    master_login = await master_auth_service.login(username=username,
                                             password=password)

    assert master_login.master_id == 2