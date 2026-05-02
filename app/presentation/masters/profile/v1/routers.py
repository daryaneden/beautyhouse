from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends
from app.presentation.jwt_service import JwtService
from app.presentation.dependencies import get_jwt_service
from app.presentation.masters.profile.v1.schemas import MasterProfileResponseSchema
from app.presentation.masters.profile.v1.schemas import MasterProfileCreateSchema
from app.application.masters.profile.use_cases.create_master_profile import CreateMasterProfileUseCase
from app.presentation.dependencies import get_create_master_profile_use_case
from app.presentation.masters.profile.v1.mappers import MasterMapper

router = APIRouter(prefix='/masters', tags = ['masters'])

@router.post('/',
             response_model=MasterProfileResponseSchema)
async def create_master_profile(create_master_profile_use_case: Annotated[CreateMasterProfileUseCase, Depends(get_create_master_profile_use_case)],
                                master_profile_create_data: MasterProfileCreateSchema,
                                jwt_service: Annotated[JwtService, Depends(get_jwt_service)]):
    master_id = await create_master_profile_use_case.execute(create_master_profile_dto=master_profile_create_data)
    access_token = jwt_service.generate_access_token(master_id=master_id)
    master = MasterProfileResponseSchema(master_id=master_id, access_token=access_token)
    return MasterMapper.to_master_profile_response_schema(master)