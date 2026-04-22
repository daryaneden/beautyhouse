from app.presentation.beauty_services.v1.schemas import BeautyServiceCreateSchema, BeautyServiceSchema
from application.beauty_services.dtos import BeautyServiceCreateDto, BeautyServiceDto

class BeautyServicesMapper:

    @staticmethod
    def to_beauty_services_create_schema(beauty_services_create_dto: BeautyServiceCreateDto) -> BeautyServiceCreateSchema:
        return BeautyServiceCreateSchema(service_name=beauty_services_create_dto.service_name,
                                        client_name=beauty_services_create_dto.client_name,
                                        date=beauty_services_create_dto.date)
    
    def to_beauty_services_schema(beauty_services_dto: BeautyServiceDto) -> BeautyServiceSchema:
        return BeautyServiceSchema (id=beauty_services_dto.id,
                                    service_name=beauty_services_dto.service_name,
                                    client_name=beauty_services_dto.client_name,
                                    date=beauty_services_dto.date,
                                    master_id=beauty_services_dto.master_id)