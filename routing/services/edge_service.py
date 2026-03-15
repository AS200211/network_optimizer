from routing.repositories.edge_repository import EdgeRepository
from routing.exceptions import EdgeAlreadyExistsException


class EdgeService:

    @staticmethod
    def list_edges():
        return EdgeRepository.get_all()

    @staticmethod
    def create_edge(data):

        source = data["source"]
        destination = data["destination"]

        if EdgeRepository.exists(source, destination):
            raise EdgeAlreadyExistsException()

        return EdgeRepository.create(data)

    @staticmethod
    def delete_edge(edge_id):
        return EdgeRepository.delete(edge_id)