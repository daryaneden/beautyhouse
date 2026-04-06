from fastapi import APIRouter
from typing import Annotated
from fastapi import Depends
from app.masters.profile.schema import MasterProfileSchema
from app.masters.auth.schema import MasterLoginSchema
from app.masters.profile.service import MasterProfileService
from dependencies import get_master_profile_service


router = APIRouter(prefix='/masters', tags = ['masters'])

@router.post('/',
             response_model=MasterLoginSchema)
async def create_master_profile(master_profile_service: Annotated[MasterProfileService, Depends(get_master_profile_service)],
                                body: MasterProfileSchema):
    return await master_profile_service.create_master_profile(body.username, body.full_name, body.password, body.email)