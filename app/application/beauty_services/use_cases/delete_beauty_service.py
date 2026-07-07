from app.domain.beauty_services.interface import BeautyServiceRepository
from app.application.beauty_services.use_cases.exceptions import ServiceNotFoundException

class DeleteBeautyServicesUsecase:

    def __init__(self, repo: BeautyServiceRepository):

        self.repo = repo

    
    async def execute(self, 
                    beauty_service_id: int) -> None:
        
        await self.repo.delete_beauty_service(beauty_service_id=beauty_service_id)
        