#принимает entities и возвращает dtos


from app.domain.masters.interface import MasterProfileRepository
from app.application.masters.auth.dtos import MasterAuthDto
from app.domain.jwt_interface import JwtProvider
from app.domain.masters.entities import MasterProfile
from app.application.masters.auth.exceptions import MasterNotFoundException, IncorrectPasswordException

class MasterAuthUseCases:
    
    def __init__(self, 
                 repo: MasterProfileRepository,
                 jwt_provider: JwtProvider):
    
      self.repo = repo
      self.jwt_provider = jwt_provider

    async def login(self,
                   username: str,
                   password: str) -> MasterAuthDto:
       
       master: MasterProfile = await self.repo.get_master_by_username(username=username)
       self._validate_auth_user(master, password)
       access_token = self.jwt_provider.generate_access_token(master_id=master.id)
       return MasterAuthDto(master_id=master.id, access_token=access_token)

    @staticmethod
    def _validate_auth_user(master: MasterProfile, password: str) -> None:

        if not master:
            raise MasterNotFoundException
        if master.password != password:
            raise IncorrectPasswordException
        