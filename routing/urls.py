from django.urls import path

from routing.views.node_views import (
    NodeCreateView,
    NodeListView,
    NodeDeleteView
)

from routing.views.edge_views import (
    EdgeCreateView,
    EdgeListView,
    EdgeDeleteView
)

from routing.views.route_views import (
    ShortestRouteView,
    RouteHistoryView
)


urlpatterns = [

    # Nodes APIs
    path("nodes", NodeCreateView.as_view(), name="create-node"),
    path("nodes/list", NodeListView.as_view(), name="list-nodes"),
    path("nodes/<int:pk>", NodeDeleteView.as_view(), name="delete-node"),

    # Edges APIs
    path("edges", EdgeCreateView.as_view(), name="create-edge"),
    path("edges/list", EdgeListView.as_view(), name="list-edges"),
    path("edges/<int:pk>", EdgeDeleteView.as_view(), name="delete-edge"),

    # Routes APIs
    path("routes/shortest", ShortestRouteView.as_view(), name="shortest-route"),
    path("routes/history", RouteHistoryView.as_view(), name="route-history"),

]