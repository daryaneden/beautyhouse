from dataclasses import dataclass
from app.masters.profile.repository import MasterProfileRepository
from app.masters.auth.schema import MasterLoginSchema
from app.settings import Settings
from app.masters.profile.models import MasterProfile
from app.exceptions import MasterNotFoundException, IncorrectPasswordException, TokenNotCorrectException, TokenExpiredException
from jose import jwt
from jose.exceptions import JWTError
from datetime import datetime as dt
from datetime import timedelta

@dataclass
class MasterAuthService():
   master_profile_repository: MasterProfileRepository
   settings: Settings

   async def login(self,
                   username: str,
                   password: str) -> MasterLoginSchema:
      master = await self.master_profile_repository.get_master_by_username(username)
      self._validate_auth_user(master, password)
      access_token = self.generate_access_token(master_id=master.id)
      return MasterLoginSchema(master_id=master.id, access_token=access_token)
   
   @staticmethod
   def _validate_auth_user(master: MasterProfile, password: str):
      if not master:
         raise MasterNotFoundException
      if master.password != password:
         raise IncorrectPasswordException
      
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

      
   
      
