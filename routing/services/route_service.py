import heapq

from routing.models import Node, Edge
from routing.repositories.route_repository import RouteRepository
from routing.exceptions import RouteNotFoundException


class RouteService:

    @staticmethod
    def shortest_path(source_name, destination_name):

        nodes = Node.objects.all()
        edges = Edge.objects.all()

        # Graph build
        graph = {node.name: [] for node in nodes}

        for edge in edges:
            graph[edge.source.name].append(
                (edge.destination.name, edge.latency)
            )

        pq = [(0, source_name, [])]
        visited = set()

        while pq:

            latency, current, path = heapq.heappop(pq)

            if current in visited:
                continue

            visited.add(current)
            path = path + [current]

            if current == destination_name:
                return latency, path

            for neighbor, weight in graph.get(current, []):
                heapq.heappush(
                    pq,
                    (latency + weight, neighbor, path)
                )

        raise RouteNotFoundException()

    @staticmethod
    def save_route(source, destination, latency, path):

        source_node = Node.objects.get(name=source)
        destination_node = Node.objects.get(name=destination)

        return RouteRepository.save_route({
            "source": source_node,
            "destination": destination_node,
            "total_latency": latency,
            "path": path
        })

    @staticmethod
    def get_history(filters):

        return RouteRepository.get_history(filters)