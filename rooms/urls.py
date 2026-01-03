from django.urls import path
from .views import RoomListCreateView

urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
]
