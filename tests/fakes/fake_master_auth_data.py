from pydantic import BaseModel

class FakeMasterLoginSchema(BaseModel):

    username: str = 'test_username'
    password: str = 'test_password'
