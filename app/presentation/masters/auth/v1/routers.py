from fastapi import APIRouter, HTTPException, status
from app.presentation.masters.auth.v1.exceptions import MasterNotFoundException, IncorrectPasswordException
from typing import Annotated 
from fastapi import Depends
from app.presentation.masters.auth.v1.schemas import MasterAuthRequestSchema
from app.application.masters.auth.use_cases import MasterAuthUseCases
from app.presentation.dependencies import get_master_auth_use_cases
from app.presentation.masters.profile.v1.mappers import MasterMapper
from app.presentation.masters.profile.v1.schemas import MasterProfileResponseSchema

router = APIRouter(prefix='/masters/auth', tags=['masters_auth'])

@router.post('/',
             response_model=MasterProfileResponseSchema)
async def login_master(master_auth_use_cases: Annotated[MasterAuthUseCases, Depends(get_master_auth_use_cases)],
                    body: MasterAuthRequestSchema
                    ):
    try:
        master = await master_auth_use_cases.login(username=body.username, password=body.password)
        return MasterMapper.to_master_profile_response_schema(master)
    except MasterNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
    except IncorrectPasswordException as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail)