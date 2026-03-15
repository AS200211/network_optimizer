from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from routing.services.route_service import RouteService
from common.pagination import RouteHistoryPagination
from routing.serializers import RouteQuerySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from routing.serializers import ShortestRouteRequestSerializer


class ShortestRouteView(APIView):

    @swagger_auto_schema(request_body=ShortestRouteRequestSerializer)
    def post(self, request):

        source = request.data.get("source")
        destination = request.data.get("destination")

        latency, path = RouteService.shortest_path(
            source,
            destination
        )

        RouteService.save_route(
            source,
            destination,
            latency,
            path
        )

        return Response({
            "total_latency": latency,
            "path": path
        }, status=status.HTTP_200_OK)


class RouteHistoryView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "source",
                openapi.IN_QUERY,
                description="Filter by source node",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                "destination",
                openapi.IN_QUERY,
                description="Filter by destination node",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                "date_from",
                openapi.IN_QUERY,
                description="Start date filter",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                "date_to",
                openapi.IN_QUERY,
                description="End date filter",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                "limit",
                openapi.IN_QUERY,
                description="Limit number of records",
                type=openapi.TYPE_INTEGER
            ),
        ]
    )
    def get(self, request):

        filters = {
            "source": request.query_params.get("source"),
            "destination": request.query_params.get("destination"),
            "date_from": request.query_params.get("date_from"),
            "date_to": request.query_params.get("date_to"),
        }

        routes = RouteService.get_history(filters)
        paginator = RouteHistoryPagination()
        page = paginator.paginate_queryset(routes, request)
        serializer = RouteQuerySerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)