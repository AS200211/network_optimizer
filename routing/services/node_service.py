from routing.repositories.node_repository import NodeRepository


class NodeService:

    @staticmethod
    def list_nodes():
        return NodeRepository.get_all()

    @staticmethod
    def create_node(data):
        return NodeRepository.create(data)

    @staticmethod
    def delete_node(node_id):
        return NodeRepository.delete(node_id)