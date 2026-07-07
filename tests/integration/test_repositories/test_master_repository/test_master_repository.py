from app.infrastructure.masters.repository import SQLAlchemyMastersRepository
from tests.fakes.fake_master_profile_data import FakeMasterProfileData
from app.infrastructure.masters.models import MasterProfile
import pytest


@pytest.mark.asyncio
class TestMasterRepository:

    @pytest.fixture
    def repo(self, test_session):

        return SQLAlchemyMastersRepository(db_session=test_session)
    
    @pytest.fixture
    def master_profile_data(self):

        return FakeMasterProfileData()
    
    async def test_create_master_profile(self, repo, master_profile_data):

        master_id = await repo.create_master_profile(master_profile_data)

        assert master_id == 1

    async def test_get_master(self, repo, master_profile_data):

        new_master_id = await repo.create_master_profile(master_profile_data)

        found_master = await repo.get_master(master_id=1)

        assert isinstance(found_master, MasterProfile)
        assert found_master.id == new_master_id

    async def test_get_master_by_username(self, repo, master_profile_data):

        await repo.create_master_profile(master_profile_data)
        new_master_profile = await repo.get_master(master_id=1)

        found_by_username = await repo.get_master_by_username(new_master_profile.username)

        assert isinstance(found_by_username, MasterProfile)
        assert new_master_profile == found_by_username






        


    
    