from app.domain.jwt_interface import JwtProvider
from app.infrastructure.exceptions import TokenNotCorrectException, TokenExpiredException
from app.setting import Settings
from jose import jwt, JWTError
from datetime import datetime as dt
from datetime import timedelta
from fastapi import security, Security, HTTPException

class JwtService(JwtProvider):

   reusable_oauth = security.HTTPBearer()

   def __init__(self, 
                 settings: Settings):

        self.settings = settings

   def generate_access_token(self, master_id: int) -> str:
      expire_date_unix = (dt.now() + timedelta(days=1)).timestamp()
      token = jwt.encode({'user_id': master_id, 'expire': expire_date_unix},
                         self.settings.JWT_SECRET_KEY,
                         algorithm=self.settings.JWT_ENCODE_ALGORITHM)
      return token 
   
   def get_master_id_from_access_token(self, access_token: str) -> int:
      try:
         payload = jwt.decode(access_token, 
                              self.settings.JWT_SECRET_KEY,
                              algorithms=[self.settings.JWT_ENCODE_ALGORITHM])
      except JWTError:
         raise TokenNotCorrectException
      if payload['expire'] < dt.now().timestamp():
         raise TokenExpiredException
      return payload['user_id']
    
   async def get_request_master_id(self, token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth)) -> int:

      try:
         master_id = self.get_master_id_from_access_token(token.credentials)
      except TokenExpiredException as e:
         raise HTTPException(
            status_code=401,
            detail=e.detail
        )
      except TokenNotCorrectException as e:
        raise HTTPException(
            status_code=401,
            detail = e.detail
        )
      return master_id
