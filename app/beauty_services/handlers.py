from fastapi import APIRouter, status, HTTPException
from app.beauty_services.schema import BeautyServiceSchema, BeautyServiceCreateSchema
from app.beauty_services.service import BeautyServiceService
from dependencies import get_beauty_services_service
from typing import Annotated
from fastapi import Depends
from dependencies import get_request_master_id
from app.exceptions import ServiceNotFoundException

router = APIRouter(prefix='/services', tags = ['services'])

@router.get('/all',
            response_model=list[BeautyServiceSchema])
async def get_beauty_services(beauty_services_service: Annotated[BeautyServiceService, Depends(get_beauty_services_service)]):
    return await beauty_services_service.get_beauty_services()

@router.post('/',
             response_model=BeautyServiceSchema)
async def create_beauty_service(beauty_services_service: Annotated[BeautyServiceService, Depends(get_beauty_services_service)],
                                service_name: str, 
                                client_name: str,
                                date: str,
                                master_id: int = Depends(get_request_master_id)
                                ):
    return await beauty_services_service.create_beauty_service(service_name = service_name, 
                                                            client_name = client_name,
                                                            date = date,
                                                            master_id = master_id)

@router.patch('/{service_id}',
              response_model=BeautyServiceSchema)
async def update_beauty_service_date(beauty_services_service: Annotated[BeautyServiceService, Depends(get_beauty_services_service)],
                                     service_id: int,
                                     date: str,
                                     master_id: int = Depends(get_request_master_id)):
    try:
        return await beauty_services_service.update_beauty_service_date(service_id=service_id,
                                                                    date=date,
                                                                    master_id=master_id)
    except ServiceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
@router.delete('/{service_id}',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete__beauty_service(beauty_services_service: Annotated[BeautyServiceService, Depends(get_beauty_services_service)],
                                     service_id: int,
                                     master_id: int = Depends(get_request_master_id)):
    try:
        return await beauty_services_service.delete_beauty_service(service_id=service_id,
                                                               master_id=master_id)
    except ServiceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )