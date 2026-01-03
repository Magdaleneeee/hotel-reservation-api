from django.urls import path
from .views import ReservationListCreateView, ReservationCancelView

urlpatterns = [
    path("reservations/", ReservationListCreateView.as_view(), name="reservation-list-create"),
    path("reservations/<int:pk>/cancel/", ReservationCancelView.as_view(), name="reservation-cancel"),
]
