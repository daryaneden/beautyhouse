from jose import jwt
import datetime as dt
from datetime import timedelta
# from app.masters.auth.schema import MasterLoginSchema
# from app.masters.auth.service import MasterAuthService
# from app.settings import Settings


def test_generate_access_token(master_auth_service,
                               settings):
    master_id = 1

    token = master_auth_service.generate_access_token(master_id)
    decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ENCODE_ALGORITHM])
    decoded_master_id = decoded_token.get('user_id')

    assert isinstance(token, str)
    assert decoded_master_id == master_id


def test_get_master_id_from_access_token(master_auth_service, settings):
    master_id = str(1)
    expire_date_unix = (dt.datetime.now() + timedelta(days=1)).timestamp()

    token = jwt.encode({'user_id': master_id, 'expire': expire_date_unix}, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ENCODE_ALGORITHM)
    decoded_id = master_auth_service.get_master_id_from_access_token(token)
    decoded_expire_date = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ENCODE_ALGORITHM]).get('expire')
    
    assert master_id == decoded_id
    assert (dt.datetime.fromtimestamp(decoded_expire_date) - dt.datetime.now()) > timedelta(hours=23)

