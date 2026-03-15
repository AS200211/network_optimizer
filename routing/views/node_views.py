from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from routing.services.node_service import NodeService
from drf_yasg.utils import swagger_auto_schema
from routing.serializers import NodeSerializer


class NodeCreateView(APIView):

    @swagger_auto_schema(request_body=NodeSerializer)
    def post(self, request):

        serializer = NodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        node = NodeService.create_node(serializer.validated_data)

        return Response(
            NodeSerializer(node).data,
            status=status.HTTP_201_CREATED
        )

class NodeListView(APIView):

    # @swagger_auto_schema(request_body=NodeSerializer)
    def get(self, request):

        nodes = NodeService.list_nodes()
        serializer = NodeSerializer(nodes, many=True)

        return Response(serializer.data)

class NodeDeleteView(APIView):

    # @swagger_auto_schema(request_body=NodeSerializer)
    def delete(self, request, pk):

        NodeService.delete_node(pk)

        return Response(
            {"message": "Node deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )