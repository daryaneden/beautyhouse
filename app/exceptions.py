class ServiceNotFoundException(Exception):
    detail = 'Service not found'

class IncorrectPasswordException(Exception):
    detail = 'Incorrect password'

class MasterNotFoundException(Exception):
    detail = 'Master not found'

class TokenNotCorrectException(Exception):
    detail = 'Incorrect access token'

class TokenExpiredException(Exception):
    detail = 'Access token has expired'