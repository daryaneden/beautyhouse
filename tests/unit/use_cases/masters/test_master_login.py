from app.domain.masters.interface import MasterProfileRepository
from app.domain.masters.entities import MasterProfile
from app.application.masters.auth.use_cases.exceptions import MasterNotFoundException, IncorrectPasswordException
from app.application.masters.auth.use_cases.master_login import MasterLoginUseCase

import pytest
from unittest.mock import AsyncMock

@pytest.mark.asyncio
class TestMasterLoginUseCase:

    @pytest.fixture
    def mock_master(self):
        master = AsyncMock()
        master.id = 1
        master.username = 'test_master'
        master.password = 'password'
        return master

    @pytest.fixture
    def mock_repo(self, mock_master):
        repo = AsyncMock(spec=MasterProfileRepository)
        repo.get_master_by_username.return_value = mock_master
        return repo

    @pytest.fixture
    def use_case(self, mock_repo):
        return MasterLoginUseCase(repo=mock_repo)

    async def test_execute_success(self, use_case, mock_repo):

        result = await use_case.execute(username='test_master', password = 'password')
        mock_repo.get_master_by_username.assert_called_once()

        assert result == 1

    async def test_execute_master_not_found(self, use_case, mock_repo):

        mock_repo.get_master_by_username.return_value =None

        with pytest.raises(MasterNotFoundException):
            await use_case.execute(username='any_master', password = 'any_password')

    async def test_execute_incorrect_password(self, use_case):

        with pytest.raises(IncorrectPasswordException):
            await use_case.execute(username='test_master', password = 'any_password')
