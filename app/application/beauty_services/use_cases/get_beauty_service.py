from app.domain.beauty_services.interface import BeautyServiceRepository
from app.domain.beauty_services.entities import BeautyService
from app.application.beauty_services.dtos import BeautyServiceDto
from app.application.beauty_services.use_cases.exceptions import ServiceNotFoundException

class GetBeautyServiceUseCase:

    def __init__(self, repo: BeautyServiceRepository):

        self.repo = repo

    async def execute(self, beauty_service_id: int) -> BeautyServiceDto:

        beauty_service: BeautyService = await self.repo.get_beauty_service(beauty_service_id=beauty_service_id)
        if not beauty_service:
            raise ServiceNotFoundException
        beauty_service_dto = BeautyServiceDto.model_validate(beauty_service)
        return beauty_service_dto