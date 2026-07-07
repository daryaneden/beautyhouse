from app.infrastructure.beauty_services.repository import SQLAlchemyBeautyServicesRepository
from app.infrastructure.beauty_services.models import BeautyService
from app.infrastructure.masters.repository import SQLAlchemyMastersRepository
from tests.fakes.fake_beauty_service_data import FakeBeautyServiceData
from tests.fakes.fake_master_profile_data import FakeMasterProfileData


import pytest
import pytest_asyncio

@pytest.mark.asyncio
class TestBeautyServiceRepository:

    @pytest.fixture
    def repo(self, test_session):

        return SQLAlchemyBeautyServicesRepository(db_session=test_session)
    
    @pytest.fixture
    def master_repo(self, test_session):

        return SQLAlchemyMastersRepository(db_session=test_session)
    
    @pytest_asyncio.fixture
    async def master_id(self, master_repo):
        master_profile = FakeMasterProfileData()
        master_id = await master_repo.create_master_profile(master_profile)
        return master_id
 
    async def test_create_beauty_service(self, repo, master_id):

        beauty_service = FakeBeautyServiceData()

        beauty_service_id = await repo.create_beauty_service(beauty_service_create_model = beauty_service,
                                        master_id = master_id)
        
        assert beauty_service_id == 1
    
    async def test_get_beauty_services(self, repo, master_id):

        beauty_service = FakeBeautyServiceData()

        await repo.create_beauty_service(beauty_service_create_model = beauty_service,
                                        master_id = master_id)
        result = await repo.get_beauty_services()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BeautyService)

    async def test_get_beauty_service(self, repo, master_id):
        
        beauty_service = FakeBeautyServiceData()
        await repo.create_beauty_service(beauty_service_create_model = beauty_service,
                                        master_id = master_id)

        result = await repo.get_beauty_service(beauty_service_id = 1)

        assert isinstance(result, BeautyService)
        assert result.service_name == 'test_service'

    async def test_get_master_beauty_service(self, repo, master_id):
        
        beauty_service = FakeBeautyServiceData()
        await repo.create_beauty_service(beauty_service_create_model = beauty_service,
                                        master_id = master_id)
        
        result = await repo.get_master_beauty_service(beauty_service_id = 1, master_id = 1)
        assert isinstance(result, BeautyService)

    async def test_update_beauty_service_date(self, repo, master_id):
        
        beauty_service = FakeBeautyServiceData()
        await repo.create_beauty_service(beauty_service_create_model = beauty_service,
                                        master_id = master_id)
        beauty_service_old_date = await repo.get_beauty_service(beauty_service_id = 1)

        beauty_service.date = 'new_date'

        await repo.update_beauty_service_date(beauty_service_update_model = beauty_service)
        beauty_service_new_date  = await repo.get_beauty_service(beauty_service_id = 1)

        assert beauty_service_new_date.date == 'new_date'
        assert beauty_service_new_date is beauty_service_old_date

