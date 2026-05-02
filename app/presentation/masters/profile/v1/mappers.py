from app.application.masters.auth.dtos import MasterAuthDto
from app.presentation.masters.profile.v1.schemas import MasterProfileResponseSchema


class MasterMapper:
    @staticmethod
    def to_master_profile_response_schema(master_auth_dto: MasterAuthDto) -> MasterProfileResponseSchema:
        return MasterProfileResponseSchema(master_id=master_auth_dto.master_id,
                                           access_token=master_auth_dto.access_token)

