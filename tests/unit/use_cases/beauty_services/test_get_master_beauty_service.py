from app.domain.beauty_services.interface import BeautyServiceRepository
from app.application.beauty_services.use_cases.get_master_beauty_service import GetMasterBeautyServiceUseCase
from app.domain.beauty_services.entities import BeautyService
from app.application.beauty_services.use_cases.exceptions import ServiceNotFoundException

import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
class TestGetMasterBeautyServiceUseCase:
    
    @pytest.fixture
    def mock_repo(self):
        repo = AsyncMock(spec=BeautyServiceRepository)
        repo.get_master_beauty_service.return_value = BeautyService(id =1,
                                                    service_name = 'test_service',
                                                    client_name = 'test',
                                                    date = 'test',
                                                    master_id = 1)
        return repo
    
    @pytest.fixture
    def use_case(self, mock_repo):
        return GetMasterBeautyServiceUseCase(repo=mock_repo)
    
    async def test_get_master_beauty_service_success(self, mock_repo, use_case):

        result = await use_case.execute(beauty_service_id=1, master_id=1)
        mock_repo.get_master_beauty_service.assert_called_once()

        assert result.service_name == 'test_service'

    async def test_get_master_beauty_service_service_not_found(self, mock_repo, use_case):

        mock_repo.get_master_beauty_service.return_value = None

        with pytest.raises(ServiceNotFoundException):
            await use_case.execute(beauty_service_id=1, master_id=1)