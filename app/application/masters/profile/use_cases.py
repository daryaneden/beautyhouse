#Здесь описывается бизнес-логика(как в сервисном слое - РЕАЛИЗАЦИЯ)
#Сценарии, заложенные в приложении


from app.application.masters.auth.dtos import MasterAuthDto
from app.domain.masters.entities import MasterProfile
from app.domain.jwt_interface import JwtProvider
from app.domain.masters.interface import MasterProfileRepository

class MasterProfileUseCases:
    
   def __init__(self, repo: MasterProfileRepository,
                jwt_provider: JwtProvider):
    
      self.repo = repo
      self.jwt_provider = jwt_provider


   async def create_master_profile (self,
                                   username: str,
                                   full_name: str,
                                   password: str,
                                   email: str) -> MasterAuthDto:
        
        master: MasterProfile = await self.repo.create_master_profile(username=username,
                                full_name=full_name,
                                password=password,
                                email=email)
        
        token = self.jwt_provider.generate_access_token(master_id=master.id)

        return MasterAuthDto(master_id=master.id,
                          access_token=token)

        

    