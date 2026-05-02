from app.domain.masters.interface import MasterProfileRepository
from app.application.masters.auth.dtos import MasterAuthDto

class GetMasterUseCase:
    
   def __init__(self, repo: MasterProfileRepository):
    
      self.repo = repo

   async def execute (self,
                      master_id: int) -> MasterAuthDto:
      
      master = await self.repo.get_master(master_id=master_id)
      return MasterAuthDto