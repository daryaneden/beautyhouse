import factory
from faker import Faker
from app.presentation.masters.profile.v1.schemas import MasterProfileCreateSchema
from app.infrastructure.masters.models import MasterProfile

faker = Faker()

class FakeMasterProfileSchema(factory.Factory):
    class Meta:
        model = MasterProfileCreateSchema

    username = 'test_username' 
    full_name = factory.LazyFunction(faker.name)
    password = 'test_password'
    email = factory.LazyFunction(faker.email)

class FakeMasterProfileData(factory.Factory):
    class Meta:
        model = MasterProfile

    username = 'test_username' 
    full_name = factory.LazyFunction(faker.name)
    password = 'test_password'
    email = factory.LazyFunction(faker.email)