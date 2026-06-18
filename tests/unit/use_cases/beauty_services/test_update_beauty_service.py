from app.domain.beauty_services.interface import BeautyServiceRepository
from app.application.beauty_services.use_cases.update_beauty_service_date import UpdateBeautyServiceDateUsecase
from app.application.beauty_services.dtos import BeautyServiceUpdateDto

import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
class TestUpdateBeautyServiceDateUseCase:

    @pytest.fixture
    def mock_beauty_service_update_dto(self):
        return BeautyServiceUpdateDto(id = 1,
                                      date = 'test_date')
    
    @pytest.fixture
    def mock_repo(self):
        repo = AsyncMock(spec=BeautyServiceRepository)
        repo.update_beauty_service_date.return_value = None
        return repo
    
    @pytest.fixture
    def use_case(self, mock_repo):
        return UpdateBeautyServiceDateUsecase(repo=mock_repo)
    
    async def test_update_beauty_service_date_success(self, mock_repo, use_case, mock_beauty_service_update_dto):

        result = await use_case.execute(mock_beauty_service_update_dto)
        mock_repo.update_beauty_service_date.assert_called_once()

        assert result == None