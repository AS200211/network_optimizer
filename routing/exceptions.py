from rest_framework.exceptions import APIException


class NodeNotFoundException(APIException):
    status_code = 404
    default_detail = "Node not found"
    default_code = "node_not_found"


class RouteNotFoundException(APIException):
    status_code = 404
    default_detail = "No route exists between given nodes"
    default_code = "route_not_found"


class EdgeAlreadyExistsException(APIException):
    status_code = 400
    default_detail = "Edge already exists"