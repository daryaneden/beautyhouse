from app.domain.beauty_services.interface import BeautyServiceRepository
from app.application.beauty_services.dtos import BeautyServiceCreateDto


class CreateBeautyServiceUsecase:

    def __init__(self, repo: BeautyServiceRepository):

        self.repo = repo

    
    async def execute(self, 
                      beauty_service_create_dto: BeautyServiceCreateDto,
                      master_id: int) -> int:
        
        beauty_service_id = await self.repo.create_beauty_service(beauty_service_create_model=beauty_service_create_dto,
                                              master_id=master_id)
        return beauty_service_id
        