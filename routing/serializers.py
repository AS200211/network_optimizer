from rest_framework import serializers
from .models import Node, Edge, RouteQuery


class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Node
        fields = ["id", "name"]


class EdgeSerializer(serializers.ModelSerializer):

    source = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Node.objects.all()
    )

    destination = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Node.objects.all()
    )

    class Meta:
        model = Edge
        fields = ["id", "source", "destination", "latency"]

    def validate_latency(self, value):
        if value <= 0:
            raise serializers.ValidationError("Latency must be greater than 0")
        return value


class RouteQuerySerializer(serializers.ModelSerializer):

    source = serializers.CharField(source="source.name")
    destination = serializers.CharField(source="destination.name")

    class Meta:
        model = RouteQuery
        fields = [
            "id",
            "source",
            "destination",
            "total_latency",
            "path",
            "created_at"
        ]

class ShortestRouteRequestSerializer(serializers.Serializer):
    source = serializers.CharField()
    destination = serializers.CharField()

def validate(self, data):

    if Edge.objects.filter(
        source=data["source"],
        destination=data["destination"]
    ).exists():

        raise serializers.ValidationError(
            "Edge already exists"
        )

    return data