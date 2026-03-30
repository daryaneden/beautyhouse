import pytest
from app.beauty_services.schema import BeautyServiceSchema
from fixtures.beauty_services.beauty_services_service import beauty_services_service


pytestmark = pytest.mark.asyncio

@pytest.mark.asyncio(loop_scope="session")
async def test_create_beauty_service(beauty_services_service=beauty_services_service):
    
    master_id = 1
    service_name = 'test_service_name' 
    client_name= 'test_client_name' 
    date= 'test_date' 

    beauty_service = await beauty_services_service.create_beauty_service(service_name = service_name, 
                                                                                client_name = client_name,
                                                                                date = date,
                                                                                master_id = master_id)
    
    assert isinstance(beauty_service, BeautyServiceSchema)
    assert beauty_service.master_id == master_id

@pytest.mark.asyncio(loop_scope="session")
async def test_get_beauty_services(beauty_services_service=beauty_services_service):

    services = await beauty_services_service.get_beauty_services()
    services_schema = [BeautyServiceSchema.model_validate(service) for service in services]

    assert isinstance(services_schema, list)
    assert isinstance(services_schema[0], BeautyServiceSchema)

@pytest.mark.asyncio(loop_scope="session")
async def test_update_beauty_service_date(beauty_services_service=beauty_services_service):
    
    service_id=2
    master_id=1
    date='7th July'

    service = await beauty_services_service.update_beauty_service_date(service_id=service_id,
                                                                       date=date,
                                                                       master_id=master_id)
    
    assert service.date == date

@pytest.mark.asyncio(loop_scope="session")
async def test_delete_beauty_service(beauty_services_service=beauty_services_service):

    service_id=2
    master_id=1

    await beauty_services_service.delete_beauty_service(service_id=service_id, 
                                                        master_id=master_id)
    services = await beauty_services_service.get_beauty_services()
    services_schema = [BeautyServiceSchema.model_validate(service) for service in services]

    assert len(services_schema) == 0
