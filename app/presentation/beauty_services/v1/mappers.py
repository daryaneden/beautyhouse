from app.presentation.beauty_services.v1.schemas import BeautyServiceCreateSchema, BeautyServiceSchema
from app.application.beauty_services.dtos import BeautyServiceCreateDto, BeautyServiceDto

class BeautyServicesMapper:

    @staticmethod
    def to_beauty_service_create_schema(beauty_service_create_dto: BeautyServiceCreateDto) -> BeautyServiceCreateSchema:
        return BeautyServiceCreateSchema(service_name=beauty_service_create_dto.service_name,
                                        client_name=beauty_service_create_dto.client_name,
                                        date=beauty_service_create_dto.date)
    
    @staticmethod
    def to_beauty_service_schema(beauty_service_dto: BeautyServiceDto) -> BeautyServiceSchema:
        return BeautyServiceSchema (id=beauty_service_dto.id,
                                    service_name=beauty_service_dto.service_name,
                                    client_name=beauty_service_dto.client_name,
                                    date=beauty_service_dto.date,
                                    master_id=beauty_service_dto.master_id)
    
    