import pytest_asyncio
from app.infrastructure.jwt_service import JwtService
from app.setting import Settings


@pytest_asyncio.fixture()
async def jwt_service():
    return JwtService(settings=Settings())