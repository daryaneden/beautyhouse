from app.beauty_services.service import BeautyServiceService
from app.settings import Settings 
from app.beauty_services.repository import BeautyServiceRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, security, Security, HTTPException
from typing import Annotated
from app.masters.profile.repository import MasterProfileRepository
from app.masters.profile.service import MasterProfileService
from app.masters.auth.service import MasterAuthService
from app.infrastructure.database.accessor import get_db_session
from app.exceptions import TokenExpiredException, TokenNotCorrectException


async def get_beauty_services_repository(db_session: AsyncSession = Depends(get_db_session)) -> BeautyServiceRepository:
    return BeautyServiceRepository(db_session)

async def get_beauty_services_service(beauty_service_repository: Annotated[BeautyServiceRepository, Depends(get_beauty_services_repository)]) -> BeautyServiceService:
    return BeautyServiceService(beauty_service_repository=beauty_service_repository)

async def get_master_profile_repository(db_session: AsyncSession = Depends(get_db_session)) -> MasterProfileRepository:
    return MasterProfileRepository(db_session)

async def get_master_auth_service(master_profile_repository: Annotated[MasterProfileRepository, Depends(get_master_profile_repository)]) -> MasterAuthService:
    return MasterAuthService(master_profile_repository=master_profile_repository, settings=Settings())

async def get_master_profile_service(master_profile_repository: Annotated[MasterProfileRepository, Depends(get_master_profile_repository)],
                                     master_auth_service: Annotated[MasterAuthService, Depends(get_master_auth_service)]) -> MasterProfileService:
    return MasterProfileService(master_profile_repository=master_profile_repository,
                                master_auth_service=master_auth_service)

reusable_oauth = security.HTTPBearer()

async def get_request_master_id(token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth),
                                auth_service: MasterAuthService = Depends(get_master_auth_service)) -> int:
    try:
        master_id = auth_service.get_master_id_from_access_token(token.credentials)
    except TokenExpiredException as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )
    except TokenNotCorrectException as e:
        raise HTTPException(
            status_code=401,
            detail = e.detail
        )
    return master_id