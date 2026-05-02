from fastapi import APIRouter, status, HTTPException
from app.presentation.beauty_services.v1.schemas import BeautyServiceSchema, BeautyServiceCreateSchema, BeautyServiceUpdateSchema
from app.application.beauty_services.use_cases.delete_beauty_service import DeleteBeautyServicesUsecase
from app.application.beauty_services.use_cases.create_beauty_service import CreateBeautyServiceUsecase
from app.application.beauty_services.use_cases.get_beauty_service import GetBeautyServiceUseCase
from app.application.beauty_services.use_cases.get_beauty_services import GetBeautyServicesUseCase
from app.application.beauty_services.use_cases.update_beauty_service_date import UpdateBeautyServiceDateUsecase
from app.application.beauty_services.use_cases.get_master_beauty_service import GetMasterBeautyServiceUseCase
from app.presentation.dependencies import get_create_beauty_service_use_case, get_delete_beauty_service_use_case, get_update_beauty_service_date_use_case, get_get_beauty_services_use_case, get_get_beauty_service_use_case, get_get_master_beauty_service_use_case
from typing import Annotated
from fastapi import Depends
from app.presentation.jwt_service import reusable_oauth
from app.presentation.dependencies import get_jwt_service
from app.presentation.dependencies import get_beauty_service_mapper
from app.presentation.beauty_services.v1.mappers import BeautyServicesMapper
from app.presentation.beauty_services.v1.exceptions import ServiceNotFoundException

router = APIRouter(prefix='/services', tags = ['services'], dependencies=[Depends(reusable_oauth)])

@router.get('/all',
            response_model=list[BeautyServiceSchema])
async def get_beauty_services(get_beauty_services_use_cases: Annotated[GetBeautyServicesUseCase, Depends(get_get_beauty_services_use_case)],
                              beauty_services_mapper: Annotated[BeautyServicesMapper, Depends(get_beauty_service_mapper)]):
    beauty_services = await get_beauty_services_use_cases.execute()
    return [beauty_services_mapper.to_beauty_service_schema(beauty_service) for beauty_service in beauty_services]

@router.post('/',
             response_model=BeautyServiceSchema)
async def create_beauty_service(create_beauty_service_use_cases: Annotated[CreateBeautyServiceUsecase, Depends(get_create_beauty_service_use_case)],
                                get_beauty_service_use_case: Annotated[GetBeautyServiceUseCase, Depends(get_get_beauty_service_use_case)],
                                beauty_service_create_data: BeautyServiceCreateSchema,
                                beauty_service_mapper: Annotated[BeautyServicesMapper, Depends(get_beauty_service_mapper)],
                                master_id: Annotated[int, Depends(get_jwt_service().get_request_master_id)]
                                ):

    beauty_service_id = await create_beauty_service_use_cases.execute(beauty_service_create_dto=beauty_service_create_data,
                                                                      master_id=master_id)
    beauty_service = await get_beauty_service_use_case.execute(beauty_service_id)
    return beauty_service_mapper.to_beauty_service_schema(beauty_service)

@router.patch('/{service_id}',
              response_model=BeautyServiceSchema)
async def update_beauty_service_date(update_beauty_service_use_case: Annotated[UpdateBeautyServiceDateUsecase, Depends(get_update_beauty_service_date_use_case)],
                                     get_beauty_service_use_case: Annotated[GetBeautyServiceUseCase, Depends(get_get_beauty_service_use_case)],
                                     get_master_beauty_service_use_case: Annotated[GetMasterBeautyServiceUseCase, Depends(get_get_master_beauty_service_use_case)],
                                     beauty_services_mapper: Annotated[BeautyServicesMapper, Depends(get_beauty_service_mapper)],
                                     beauty_service_update_schema: BeautyServiceUpdateSchema,
                                     master_id: Annotated[int, Depends(get_jwt_service().get_request_master_id)]
                                     ):
    
    try:
        await get_master_beauty_service_use_case.execute(beauty_service_id=beauty_service_update_schema.id,
                                                            master_id=master_id)
        await update_beauty_service_use_case.execute(beauty_service_update_dto=beauty_service_update_schema)
        beauty_service = await get_beauty_service_use_case.execute(beauty_service_id=beauty_service_update_schema.id)
        return beauty_services_mapper.to_beauty_service_schema(beauty_service)
    except ServiceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
    
@router.delete('/{service_id}',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_beauty_service(delete_beauty_service_use_case: Annotated[DeleteBeautyServicesUsecase, Depends(get_delete_beauty_service_use_case)],
                                get_master_beauty_service_use_case: Annotated[GetMasterBeautyServiceUseCase, Depends(get_get_master_beauty_service_use_case)],
                                beauty_service_id: int,
                                master_id: Annotated[int, Depends(get_jwt_service().get_request_master_id)]
                                ):
    try:
        await get_master_beauty_service_use_case.execute(beauty_service_id=beauty_service_id,
                                                            master_id=master_id)
        return await delete_beauty_service_use_case.execute(beauty_service_id=beauty_service_id)
    except ServiceNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )