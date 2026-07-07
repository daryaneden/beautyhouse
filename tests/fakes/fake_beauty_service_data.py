import factory
from faker import Faker
from app.presentation.beauty_services.v1.schemas import BeautyServiceCreateSchema, BeautyServiceUpdateSchema
from app.infrastructure.beauty_services.models import BeautyService

faker = Faker()

class FakeBeautyServiceData(factory.Factory):
    class Meta:
        model = BeautyService


    id = 1
    service_name = 'test_service'
    client_name = 'test_client'
    date = faker.date()
    master_id = 1

class FakeBeautyServiceCreateSchema(factory.Factory):
    class Meta:
        model = BeautyServiceCreateSchema

    service_name = 'test_service'
    client_name = 'test_client'
    date = faker.date()

class FakeBeautyServiceUpdateSchema(factory.Factory):
    class Meta:
        model = BeautyServiceUpdateSchema
    
    id = 1
    date = faker.date()