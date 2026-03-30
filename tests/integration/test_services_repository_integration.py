import pytest
from app.beauty_services.models import BeautyServices
from app.beauty_services.schema import BeautyServiceSchema
from tests.fixtures.beauty_services.beauty_services_repository import beauty_services_repository


pytestmark = pytest.mark.asyncio

@pytest.mark.asyncio(loop_scope="session")
async def test_create_beauty_service(beauty_services_repository=beauty_services_repository):
    master_id = 1
    service_name = 'test_service_name' 
    client_name= 'test_client_name' 
    date= 'test_date' 

    service_id = await beauty_services_repository.create_beauty_service(service_name=service_name, 
                                                                        client_name=client_name,
                                                                        master_id=master_id,
                                                                        date=date)
    
    assert service_id == 1

@pytest.mark.asyncio(loop_scope="session")
async def test_get_beauty_service(beauty_services_repository=beauty_services_repository):
    service_id = 1

    await beauty_services_repository.get_beauty_service(service_id=service_id)

@pytest.mark.asyncio(loop_scope="session")
async def test_get_beauty_services(beauty_services_repository):
    services = await beauty_services_repository.get_beauty_services()

    assert isinstance(services, list)
    assert isinstance(services[0], BeautyServices)

@pytest.mark.asyncio(loop_scope="session")
async def test_get_master_beauty_service(beauty_services_repository=beauty_services_repository):
    service_id = 1
    master_id = 1

    service = await beauty_services_repository.get_master_beauty_service(service_id = service_id,
                                                                         master_id = master_id)
    
    assert isinstance(service, BeautyServices)

@pytest.mark.asyncio(loop_scope="session")
async def test_update_beauty_service_date(beauty_services_repository=beauty_services_repository):
    service_id = 1
    date = '1st March'

    updated_service = await beauty_services_repository.update_beauty_service_date(service_id=service_id,
                                                                            date=date)
    
    assert updated_service.date == date

@pytest.mark.asyncio(loop_scope="session")
async def test_delete_beauty_service(beauty_services_repository=beauty_services_repository):
    service_id = 1

    await beauty_services_repository.delete_beauty_service(service_id=service_id)

    services = await beauty_services_repository.get_beauty_services()
    services_schema = [BeautyServiceSchema.model_validate(service) for service in services]

    assert len(services_schema) == 0