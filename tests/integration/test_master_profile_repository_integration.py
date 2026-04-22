import pytest
from app.domain.masters.entities import MasterProfile


pytestmark = pytest.mark.asyncio

@pytest.mark.asyncio(loop_scope="session")
async def test_create_master_profile(master_profile_repository):
    username='test_username'
    full_name='test_full_name'
    password='test_password'
    email='test_email'

    master = await master_profile_repository.create_master_profile(username=username,
                                                                    full_name=full_name,
                                                                    password=password,
                                                                    email=email)
    
    assert isinstance(master, MasterProfile)


@pytest.mark.asyncio(loop_scope="session")
async def test_get_master_by_username(master_profile_repository):
    username='test_username'
    master_id = 1

    master = await master_profile_repository.get_master_by_username(username=username)

    assert master.id == master_id

