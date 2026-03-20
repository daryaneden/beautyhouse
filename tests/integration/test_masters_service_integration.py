import pytest
from tests.fixture.infrastructure import get_test_session

pytestmark = pytest.mark.asyncio

@pytest.mark.asyncio(loop_scope="session")
async def test_create_master_profile(master_profile_service):
    username = 'test_username'
    full_name = 'test_full_name'
    password = 'test_password'
    email = 'test_email'

    master_id = await master_profile_service.create_master_profile(username=username, 
                                                                   full_name=full_name, 
                                                                   password=password, 
                                                                   email=email)

    assert master_id is not None
