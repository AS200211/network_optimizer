from routing.models import Edge


class EdgeRepository:

    @staticmethod
    def get_all():
        return Edge.objects.select_related("source", "destination").all()

    @staticmethod
    def create(data):
        return Edge.objects.create(**data)

    @staticmethod
    def delete(edge_id):
        edge = Edge.objects.get(id=edge_id)
        edge.delete()
        return True

    @staticmethod
    def exists(source, destination):
        return Edge.objects.filter(
            source=source,
            destination=destination
        ).exists()