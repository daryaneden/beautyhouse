from app.domain.masters.interface import MasterProfileRepository
from app.application.masters.profile.use_cases.create_master_profile import CreateMasterProfileUseCase

import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
class TestCreateMasterProfileUseCase:

    @pytest.fixture
    def mock_create_master_profile_dto(self):
        create_master_profile_dto = AsyncMock(username = 'test',
                                            full_name = 'test',
                                            password = 'test',
                                            email = 'test')
        
        return create_master_profile_dto
        

    @pytest.fixture
    def mock_repo(self):

        repo = AsyncMock(spec=MasterProfileRepository)
        repo.create_master_profile.return_value = 1
        return repo
    
    @pytest.fixture
    def use_case(self, mock_repo):
        return CreateMasterProfileUseCase(repo=mock_repo)
    
    async def test_create_master_profile(self, use_case, mock_create_master_profile_dto, mock_repo):

        result = await use_case.execute(mock_create_master_profile_dto)
        mock_repo.create_master_profile.assert_called_once()

        assert result == 1