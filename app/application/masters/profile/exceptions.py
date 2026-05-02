class IncorrectTokenException(Exception):
    detail = 'Incorrect access token'

class TokenExpiredException(Exception):
    detail = 'Access token has expired'