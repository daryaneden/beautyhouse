import pytest
from tests.fixture.infrastructure import get_test_session
from app.masters.profile.service import MasterProfileService
from app.masters.profile.repository import MasterProfileRepository

pytestmark = pytest.mark.asyncio

@pytest.mark.asyncio
async def test_create_master_profile(master_profile_service: MasterProfileService):
    username = 'test_username'
    full_name = 'test_full_name'
    password = 'test_password'
    email = 'test_email'

    master_id = await master_profile_service.create_master_profile(username=username, 
                                                                   full_name=full_name, 
                                                                   password=password, 
                                                                   email=email)

    assert master_id is not None


# @pytest.mark.asyncio
# async def test_create_master_profile(master_profile_repository: MasterProfileRepository):
#     username = 'test_username'
#     full_name = 'test_full_name'
#     password = 'test_password'
#     email = 'test@mail.ru'

#     master_id = await master_profile_repository.create_master_profile(username=username, 
#                                                                    full_name=full_name, 
#                                                                    password=password, 
#                                                                    email=email)

#     assert isinstance(master_id, int) 