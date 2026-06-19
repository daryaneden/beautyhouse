from app.infrastructure.beauty_services.repository import SQLAlchemyBeautyServicesRepository
from app.infrastructure.beauty_services.models import BeautyService
from app.infrastructure.masters.repository import SQLAlchemyMastersRepository
from tests.fakes.fake_beauty_service_data import BeautyServiceData
from tests.fakes.fake_master_profile_data import MasterProfileData
from tests.conftest import get_test_session

import pytest

@pytest.mark.asyncio
class TestBeautyServiceRepository:

    @pytest.fixture
    def repo(self, get_test_session):

        return SQLAlchemyBeautyServicesRepository(db_session=get_test_session)
    
    @pytest.fixture
    def master_repo(self, get_test_session):

        return SQLAlchemyMastersRepository(db_session=get_test_session)
    
    async def test_get_beauty_services(self, repo, master_repo):

        test_master = MasterProfileData()
        test_record = BeautyServiceData()

        await master_repo.create_master_profile( master_profile_create_model = test_master)

        await repo.create_beauty_service(beauty_service_create_model = test_record,
                                        master_id = 1)

        result = await repo.get_beauty_services()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BeautyService)

    # async def test_get_beauty_service(self, repo):

    #     result = await repo.get_beauty_service(beauty_service_id = 1)

    #     assert result is not None