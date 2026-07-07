from app.domain.beauty_services.interface import BeautyServiceRepository
from app.application.beauty_services.use_cases.get_beauty_service import GetBeautyServiceUseCase
from app.application.beauty_services.dtos import BeautyServiceDto
from app.domain.beauty_services.entities import BeautyService

import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
class TestGetBeautyServiceUseCase:
    
    @pytest.fixture
    def mock_repo(self):
        repo = AsyncMock(spec=BeautyServiceRepository)
        repo.get_beauty_service.return_value = BeautyService(id =1,
                                                    service_name = 'test_service',
                                                    client_name = 'test',
                                                    date = 'test',
                                                    master_id = 1)
        return repo
    
    @pytest.fixture
    def use_case(self, mock_repo):
        return GetBeautyServiceUseCase(repo=mock_repo)
    
    async def test_get_beauty_service(self, mock_repo, use_case):

        result = await use_case.execute(beauty_service_id=1)
        mock_repo.get_beauty_service.assert_called_once()

        assert isinstance(result, BeautyServiceDto)
        assert result.service_name == 'test_service'


