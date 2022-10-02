class DomainException(Exception):
    pass

class ServiceException(Exception):
    pass

class RepositoryException(Exception):
    pass

class VehicleLimit(ServiceException):
    pass

class CustomerNotFound(ServiceException):
    pass