from fastapi import APIRouter, status, HTTPException
from app.presentation.beauty_services.v1.schemas import BeautyServiceSchema
from app.application.beauty_services.use_cases import BeautyServicesUsecases
from app.presentation.dependencies import get_beauty_services_use_cases
from typing import Annotated
from fastapi import Depends
from app.infrastructure.jwt_service import JwtService
from app.exceptions import ServiceNotFoundException
from app.presentation.dependencies import get_jwt_service
from app.presentation.dependencies import get_beauty_services_mapper
from app.presentation.beauty_services.v1.mappers import BeautyServicesMapper
from app.presentation.beauty_services.v1.exceptions import ServiceNotFoundException

router = APIRouter(prefix='/services', tags = ['services'])

@router.get('/all',
            response_model=list[BeautyServiceSchema])
async def get_beauty_services(beauty_services_use_cases: Annotated[BeautyServicesUsecases, Depends(get_beauty_services_use_cases)],
                              beauty_services_mapper: Annotated[BeautyServicesMapper, Depends(get_beauty_services_mapper)]):
    beauty_services = await beauty_services_use_cases.get_beauty_services()
    return [beauty_services_mapper.to_beauty_services_schema(beauty_service) for beauty_service in beauty_services]

@router.post('/',
             response_model=BeautyServiceSchema)
async def create_beauty_service(beauty_services_use_cases: Annotated[BeautyServicesUsecases, Depends(get_beauty_services_use_cases)],
                                jwt_service: Annotated[JwtService, Depends(get_jwt_service)],
                                beauty_services_mapper: Annotated[BeautyServicesMapper, Depends(get_beauty_services_mapper)],
                                service_name: str, 
                                client_name: str,
                                date: str,
                                master_id: int
                                ):
    master_id = await jwt_service.get_request_master_id()
    beauty_service = await beauty_services_use_cases.create_beauty_service(service_name = service_name, 
                                                            client_name = client_name,
                                                            date = date,
                                                            master_id = master_id)
    return beauty_services_mapper.to_beauty_services_schema(beauty_service)

@router.patch('/{service_id}',
              response_model=BeautyServiceSchema)
async def update_beauty_service_date(beauty_services_use_cases: Annotated[BeautyServicesUsecases, Depends(get_beauty_services_use_cases)],
                                     beauty_services_mapper: Annotated[BeautyServicesMapper, Depends(get_beauty_services_mapper)],
                                     service_id: int,
                                     date: str,
                                     master_id: int = Depends(JwtService.get_request_master_id)):
    try:
        beauty_service = await beauty_services_use_cases.update_beauty_service_date(service_id=service_id,
                                                                    date=date,
                                                                    master_id=master_id)
        return beauty_services_mapper.to_beauty_services_schema(beauty_service)
    except ServiceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
@router.delete('/{service_id}',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete__beauty_service(beauty_services_use_cases: Annotated[BeautyServicesUsecases, Depends(get_beauty_services_use_cases)],
                                jwt_service: Annotated[JwtService, Depends(get_jwt_service)],
                                service_id: int,
                                master_id: int):
    try:
        master_id = await jwt_service.get_request_master_id()
        return await beauty_services_use_cases.delete_beauty_service(service_id=service_id,
                                                               master_id=master_id)
    except ServiceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )