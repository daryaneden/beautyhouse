from app.domain.beauty_services.interface import BeautyServiceRepository
from app.application.beauty_services.use_cases.delete_beauty_service import DeleteBeautyServicesUsecase

import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
class TestDeleteBeautyServiceUseCase:

    @pytest.fixture
    def mock_repo(self):
        repo = AsyncMock(spec=BeautyServiceRepository)
        repo.delete_beauty_service.return_value = None
        return repo
    
    @pytest.fixture
    def use_case(self, mock_repo):
        return DeleteBeautyServicesUsecase(repo=mock_repo)
    
    async def test_delete_beauty_service(self, use_case, mock_repo):

        result = await use_case.execute(beauty_service_id=1)
        mock_repo.delete_beauty_service.assert_called_once()

        assert result == None