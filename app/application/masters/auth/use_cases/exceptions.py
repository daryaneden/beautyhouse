class MasterNotFoundException(Exception):
    detail = 'Master not found'

class IncorrectPasswordException(Exception):
    detail = 'Incorrect password'