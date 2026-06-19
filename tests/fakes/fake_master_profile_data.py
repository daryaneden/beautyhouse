import factory
from faker import Faker
from app.infrastructure.masters.models import MasterProfile

faker = Faker()

class MasterProfileData(factory.Factory):
    class Meta:
        model = MasterProfile

    id = 1
    username = factory.LazyFunction(faker.user_name)
    full_name = factory.LazyFunction(faker.name)
    password = factory.LazyFunction(faker.password)
    email = factory.LazyFunction(faker.email)