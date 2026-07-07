from app.domain.masters.interface import MasterProfileRepository
from app.domain.masters.entities import MasterProfile
from app.application.masters.auth.use_cases.exceptions import MasterNotFoundException, IncorrectPasswordException
from app.application.masters.auth.dtos import MasterLoginDataDto

class MasterLoginUseCase:
    
    def __init__(self, 
                 repo: MasterProfileRepository):
    
      self.repo = repo

    async def execute(self,
                   master_login_data_dto: MasterLoginDataDto) -> int:
       
       master = await self.repo.get_master_by_username(username=master_login_data_dto.username)
       self._validate_auth_user(master, master_login_data_dto.password)
       return master.id

    @staticmethod
    def _validate_auth_user(master: MasterProfile, password: str) -> None:

        if not master:
            raise MasterNotFoundException
        if master.password != password:
            raise IncorrectPasswordException
        