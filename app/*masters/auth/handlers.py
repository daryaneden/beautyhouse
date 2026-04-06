from fastapi import APIRouter, HTTPException, status
from app.exceptions import MasterNotFoundException, IncorrectPasswordException
from typing import Annotated 
from fastapi import Depends
from app.masters.profile.schema import MasterProfileSchema
from app.masters.auth.schema import MasterLoginSchema
from app.masters.auth.service import MasterAuthService
from dependencies import get_master_auth_service

router = APIRouter(prefix='/masters/auth', tags=['masters_auth'])

@router.post('/',
             response_model=MasterLoginSchema)
async def login_master(master_auth_service: Annotated[MasterAuthService, Depends(get_master_auth_service)],
                      body: MasterProfileSchema):
    try:
        return await master_auth_service.login(username=body.username, password=body.password)
    except MasterNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.detail
        )
    except IncorrectPasswordException as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail)