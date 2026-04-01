from dataclasses import dataclass
from masters.profile.repository import MasterProfileRepository
from masters.auth.schema import MasterLoginSchema
from masters.auth.service import MasterAuthService

@dataclass
class MasterProfileService():
   master_profile_repository: MasterProfileRepository
   master_auth_service: MasterAuthService

   async def create_master_profile(self,
                                   username: str,
                                   full_name: str,
                                   password: str,
                                   email: str) -> MasterLoginSchema:
      master_profile = await self.master_profile_repository.create_master_profile(username=username, 
                                                                                  full_name=full_name, 
                                                                                  password=password, 
                                                                                  email=email)
      access_token = self.master_auth_service.generate_access_token(master_id=master_profile.id)
      return MasterLoginSchema(master_id=master_profile.id, access_token=access_token)