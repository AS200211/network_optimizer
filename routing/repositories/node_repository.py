from routing.models import Node


class NodeRepository:

    @staticmethod
    def get_all():
        return Node.objects.all()

    @staticmethod
    def get_by_id(node_id):
        return Node.objects.get(id=node_id)

    @staticmethod
    def create(data):
        return Node.objects.create(**data)

    @staticmethod
    def delete(node_id):
        node = Node.objects.get(id=node_id)
        node.delete()
        return True