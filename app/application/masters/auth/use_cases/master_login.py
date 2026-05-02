from app.domain.masters.interface import MasterProfileRepository
from app.domain.masters.entities import MasterProfile
from app.application.masters.auth.use_cases.exceptions import MasterNotFoundException, IncorrectPasswordException

class MasterLoginUseCase:
    
    def __init__(self, 
                 repo: MasterProfileRepository):
    
      self.repo = repo

    async def execute(self,
                   username: str,
                   password: str) -> int:
       
       master = await self.repo.get_master_by_username(username=username)
       self._validate_auth_user(master, password)
       return master.id

    @staticmethod
    def _validate_auth_user(master: MasterProfile, password: str) -> None:

        if not master:
            raise MasterNotFoundException
        if master.password != password:
            raise IncorrectPasswordException
        