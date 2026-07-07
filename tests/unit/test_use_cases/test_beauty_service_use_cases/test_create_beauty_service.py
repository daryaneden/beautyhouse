from app.domain.beauty_services.interface import BeautyServiceRepository
from app.application.beauty_services.use_cases.create_beauty_service import CreateBeautyServiceUsecase
from app.application.beauty_services.dtos import BeautyServiceCreateDto

import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
class TestCreateBeautyServiceUseCase:

    @pytest.fixture
    def mock_beauty_service_create_dto(self):
        return BeautyServiceCreateDto(service_name = 'test',
                                            client_name = 'test',
                                            date = 'test')

    @pytest.fixture
    def mock_repo(self):
        repo = AsyncMock(spec=BeautyServiceRepository)
        repo.create_beauty_service.return_value = 1
        return repo

    @pytest.fixture
    def use_case(self, mock_repo):
        return CreateBeautyServiceUsecase(repo=mock_repo)
    
    async def test_create_beauty_service(self, use_case, mock_repo, mock_beauty_service_create_dto):

        result = await use_case.execute(mock_beauty_service_create_dto, master_id=1)
        mock_repo.create_beauty_service.assert_called_once()

        assert result == 1
    

    