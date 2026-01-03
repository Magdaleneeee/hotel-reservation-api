from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        qs = Room.objects.all()
        capacity = self.request.query_params.get('capacity')
        if capacity:
            qs = qs.filter(capacity__gte=capacity)
        return qs
