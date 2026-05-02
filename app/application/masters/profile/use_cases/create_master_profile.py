from app.domain.masters.interface import MasterProfileRepository
from app.application.masters.profile.dtos import CreateMasterProfileDto

class CreateMasterProfileUseCase:
    
   def __init__(self, repo: MasterProfileRepository):
    
      self.repo = repo


   async def execute (self,
                      create_master_profile_dto: CreateMasterProfileDto) -> int:
        
      master_id = await self.repo.create_master_profile(master_profile_create_model=create_master_profile_dto)
      return master_id

        

    