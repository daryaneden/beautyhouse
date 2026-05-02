from app.domain.beauty_services.interface import BeautyServiceRepository
from app.domain.beauty_services.entities import BeautyService
from app.application.beauty_services.dtos import BeautyServiceDto


class GetBeautyServicesUseCase:

    def __init__(self, repo: BeautyServiceRepository):

        self.repo = repo

    async def execute(self) -> list[BeautyServiceDto]:

        services: BeautyService = await self.repo.get_beauty_services()
        services_dto = [BeautyServiceDto.model_validate(service) for service in services]
        return services_dto