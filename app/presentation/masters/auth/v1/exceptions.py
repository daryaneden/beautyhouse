class IncorrectPasswordException(Exception):
    detail = 'Incorrect password'

class MasterNotFoundException(Exception):
    detail = 'Master not found'