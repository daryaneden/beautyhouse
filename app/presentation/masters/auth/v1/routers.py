from fastapi import APIRouter, HTTPException, status
from app.presentation.masters.auth.v1.exceptions import MasterNotFoundException, IncorrectPasswordException
from typing import Annotated 
from fastapi import Depends
from app.presentation.masters.auth.v1.schemas import MasterLoginSchema
from app.application.masters.auth.use_cases.master_login import MasterLoginUseCase
from app.presentation.dependencies import get_master_login_use_case
from app.presentation.masters.profile.v1.mappers import MasterMapper
from app.presentation.masters.profile.v1.schemas import MasterProfileResponseSchema
from app.presentation.jwt_service import JwtService
from app.presentation.dependencies import get_jwt_service


router = APIRouter(prefix='/masters/auth', tags=['masters_auth'])

@router.post('/',
             response_model=MasterProfileResponseSchema)
async def login_master(master_login_use_case: Annotated[MasterLoginUseCase, Depends(get_master_login_use_case)],
                    master_login_schema: MasterLoginSchema,
                    jwt_service: Annotated[JwtService, Depends(get_jwt_service)]
                    ):
    try:
        master_id = await master_login_use_case.execute(master_login_data_dto=master_login_schema)
        access_token = jwt_service.generate_access_token(master_id=master_id)
        master = MasterProfileResponseSchema(master_id=master_id, access_token=access_token)
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