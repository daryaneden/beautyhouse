from app.infrastructure.db import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import Annotated
from app.domain.masters.interface import MasterProfileRepository
from app.infrastructure.beauty_services.repository import SQLAlchemyBeautyServicesRepository
from app.application.beauty_services.use_cases import BeautyServicesUsecases
from app.infrastructure.masters.repository import SQLAlchemyMastersRepository
from app.application.masters.profile.use_cases import MasterProfileUseCases
from app.application.masters.auth.use_cases import MasterAuthUseCases
from app.infrastructure.jwt_service import JwtService
from app.presentation.masters.profile.v1.mappers import MasterMapper
from app.presentation.beauty_services.v1.mappers import BeautyServicesMapper
from app.setting import Settings

async def get_master_mapper():
    return MasterMapper()

async def get_beauty_services_mapper():
    return BeautyServicesMapper()

async def get_jwt_service():
    return JwtService()

async def get_beauty_services_repository(db_session: AsyncSession = Depends(get_db_session)) -> SQLAlchemyBeautyServicesRepository:
    return SQLAlchemyBeautyServicesRepository(db_session)

async def get_beauty_services_use_cases(beauty_service_repository: Annotated[SQLAlchemyBeautyServicesRepository, Depends(get_beauty_services_repository)]) -> BeautyServicesUsecases:
    return BeautyServicesUsecases(beauty_service_repository=beauty_service_repository)

async def get_master_profile_repository(db_session: AsyncSession = Depends(get_db_session)) -> MasterProfileRepository:
    return SQLAlchemyMastersRepository(db_session=db_session)

async def get_master_auth_use_cases(master_profile_repository: Annotated[MasterProfileRepository, Depends(get_master_profile_repository)]) -> MasterAuthUseCases:
    return MasterAuthUseCases(repo=master_profile_repository,
                                jwt_provider=JwtService(settings=Settings()))

async def get_master_profile_use_cases(master_profile_repository: Annotated[MasterProfileRepository, Depends(get_master_profile_repository)]) -> MasterProfileUseCases:
    return MasterProfileUseCases(repo=master_profile_repository,
                                jwt_provider=JwtService(settings=Settings()))
