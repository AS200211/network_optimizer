from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from routing.services.edge_service import EdgeService
from drf_yasg.utils import swagger_auto_schema
from routing.serializers import EdgeSerializer


class EdgeCreateView(APIView):

    @swagger_auto_schema(request_body=EdgeSerializer)
    def post(self, request):

        serializer = EdgeSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        edge = EdgeService.create_edge(serializer.validated_data)

        return Response(
            EdgeSerializer(edge).data,
            status=status.HTTP_201_CREATED
        )

class EdgeListView(APIView):

    def get(self, request):

        edges = EdgeService.list_edges()

        serializer = EdgeSerializer(edges, many=True)

        return Response(serializer.data)

class EdgeDeleteView(APIView):

    def delete(self, request, pk):

        EdgeService.delete_edge(pk)

        return Response(
            {"message": "Edge deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )