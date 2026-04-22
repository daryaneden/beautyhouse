from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends

from app.presentation.masters.profile.v1.schemas import MasterProfileResponseSchema
from app.presentation.masters.profile.v1.schemas import MasterProfileRequestSchema
from app.application.masters.profile.use_cases import MasterProfileUseCases
from app.presentation.dependencies import get_master_profile_use_cases
from app.presentation.masters.profile.v1.mappers import MasterMapper

router = APIRouter(prefix='/masters', tags = ['masters'])

@router.post('/',
             response_model=MasterProfileResponseSchema)
async def create_master_profile(master_profile_use_cases: Annotated[MasterProfileUseCases, Depends(get_master_profile_use_cases)],
                                body: MasterProfileRequestSchema):
    master = await master_profile_use_cases.create_master_profile(body.username, body.full_name, body.password, body.email)
    return MasterMapper.to_master_profile_response_schema(master)