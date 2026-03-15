from routing.models import RouteQuery


class RouteRepository:

    @staticmethod
    def save_route(data):
        return RouteQuery.objects.create(**data)

    @staticmethod
    def get_history(filters):

        queryset = RouteQuery.objects.select_related(
            "source",
            "destination"
        ).order_by("-created_at")

        if filters.get("source"):
            queryset = queryset.filter(
                source__name=filters["source"]
            )

        if filters.get("destination"):
            queryset = queryset.filter(
                destination__name=filters["destination"]
            )

        if filters.get("date_from"):
            queryset = queryset.filter(
                created_at__gte=filters["date_from"]
            )

        if filters.get("date_to"):
            queryset = queryset.filter(
                created_at__lte=filters["date_to"]
            )

        if filters.get("limit"):
            queryset = queryset[: int(filters["limit"])]

        return queryset