from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Edge(models.Model):
    source = models.ForeignKey(
        Node,
        related_name="outgoing_edges",
        on_delete=models.CASCADE
    )

    destination = models.ForeignKey(
        Node,
        related_name="incoming_edges",
        on_delete=models.CASCADE
    )

    latency = models.FloatField()

    class Meta:
        unique_together = ("source", "destination")

    def __str__(self):
        return f"{self.source} -> {self.destination} ({self.latency})"

class RouteQuery(models.Model):
    source = models.ForeignKey(
        Node,
        related_name="route_source",
        on_delete=models.CASCADE
    )

    destination = models.ForeignKey(
        Node,
        related_name="route_destination",
        on_delete=models.CASCADE
    )

    total_latency = models.FloatField()

    path = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)