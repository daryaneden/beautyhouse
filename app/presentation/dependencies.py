from app.infrastructure.db import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import Annotated
from app.domain.masters.interface import MasterProfileRepository
from app.infrastructure.beauty_services.repository import SQLAlchemyBeautyServicesRepository
from app.application.beauty_services.use_cases.delete_beauty_service import DeleteBeautyServicesUsecase
from app.application.beauty_services.use_cases.create_beauty_service import CreateBeautyServiceUsecase
from app.application.beauty_services.use_cases.get_beauty_service import GetBeautyServiceUseCase
from app.application.beauty_services.use_cases.get_beauty_services import GetBeautyServicesUseCase
from app.application.beauty_services.use_cases.update_beauty_service_date import UpdateBeautyServiceDateUsecase
from app.application.beauty_services.use_cases.get_master_beauty_service import GetMasterBeautyServiceUseCase
from app.infrastructure.masters.repository import SQLAlchemyMastersRepository
from app.application.masters.profile.use_cases.create_master_profile import CreateMasterProfileUseCase
from app.application.masters.auth.use_cases.master_login import MasterLoginUseCase
from app.presentation.jwt_service import JwtService
from app.presentation.masters.profile.v1.mappers import MasterMapper
from app.presentation.beauty_services.v1.mappers import BeautyServicesMapper
from app.setting import Settings

async def get_master_mapper():
    return MasterMapper()

async def get_beauty_service_mapper():
    return BeautyServicesMapper()

def get_jwt_service():
    return JwtService(settings=Settings())

async def get_beauty_service_repository(db_session: Annotated[AsyncSession, Depends(get_db_session)]) -> SQLAlchemyBeautyServicesRepository:
    return SQLAlchemyBeautyServicesRepository(db_session)

async def get_get_master_beauty_service_use_case(beauty_service_repository: Annotated[SQLAlchemyBeautyServicesRepository, Depends(get_beauty_service_repository)]) -> SQLAlchemyBeautyServicesRepository:
    return GetMasterBeautyServiceUseCase(repo=beauty_service_repository)

async def get_delete_beauty_service_use_case(beauty_service_repository: Annotated[SQLAlchemyBeautyServicesRepository, Depends(get_beauty_service_repository)]) -> DeleteBeautyServicesUsecase:
    return DeleteBeautyServicesUsecase(repo=beauty_service_repository)

async def get_create_beauty_service_use_case(beauty_service_repository: Annotated[SQLAlchemyBeautyServicesRepository, Depends(get_beauty_service_repository)]) -> CreateBeautyServiceUsecase:
    return CreateBeautyServiceUsecase(repo=beauty_service_repository)

async def get_get_beauty_service_use_case(beauty_service_repository: Annotated[SQLAlchemyBeautyServicesRepository, Depends(get_beauty_service_repository)]) -> GetBeautyServiceUseCase:
    return GetBeautyServiceUseCase(repo=beauty_service_repository)

async def get_get_beauty_services_use_case(beauty_service_repository: Annotated[SQLAlchemyBeautyServicesRepository, Depends(get_beauty_service_repository)]) -> GetBeautyServicesUseCase:
    return GetBeautyServicesUseCase(repo=beauty_service_repository)

async def get_update_beauty_service_date_use_case(beauty_service_repository: Annotated[SQLAlchemyBeautyServicesRepository, Depends(get_beauty_service_repository)]) -> UpdateBeautyServiceDateUsecase:
    return UpdateBeautyServiceDateUsecase(repo=beauty_service_repository)

async def get_master_profile_repository(db_session: Annotated[AsyncSession, Depends(get_db_session)]) -> MasterProfileRepository:
    return SQLAlchemyMastersRepository(db_session=db_session)

async def get_master_login_use_case(master_profile_repository: Annotated[MasterProfileRepository, Depends(get_master_profile_repository)]) -> MasterLoginUseCase:
    return MasterLoginUseCase(repo=master_profile_repository)

async def get_create_master_profile_use_case(master_profile_repository: Annotated[MasterProfileRepository, Depends(get_master_profile_repository)]) -> CreateMasterProfileUseCase:
    return CreateMasterProfileUseCase(repo=master_profile_repository)
