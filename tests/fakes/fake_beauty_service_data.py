import factory
from faker import Faker
from app.infrastructure.beauty_services.models import BeautyService

faker = Faker()

class BeautyServiceData(factory.Factory):
    class Meta:
        model = BeautyService

    id = factory.LazyFunction(faker.uuid4)
    service_name = 'test_service'
    client_name = 'test_client'
    date = faker.date()
    master_id = factory.LazyFunction(faker.uuid4)