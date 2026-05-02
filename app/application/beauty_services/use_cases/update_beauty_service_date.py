from app.domain.beauty_services.interface import BeautyServiceRepository
from app.application.beauty_services.dtos import BeautyServiceUpdateDto



class UpdateBeautyServiceDateUsecase:

    def __init__(self, repo: BeautyServiceRepository):

        self.repo = repo

    async def execute(self, 
                      beauty_service_update_dto: BeautyServiceUpdateDto) -> None:
        
        await self.repo.update_beauty_service_date(beauty_service_update_model=beauty_service_update_dto)