from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Reservation
from .serializers import ReservationSerializer


class ReservationListCreateView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        reservation = serializer.save(user=self.request.user)
        reservation.room.is_available = False
        reservation.room.save()


class ReservationCancelView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            reservation = Reservation.objects.get(pk=pk, user=request.user)
            reservation.status = "cancelled"
            reservation.save()

            return Response(
                {"message": "Reservation cancelled successfully"},
                status=status.HTTP_200_OK
            )
        except Reservation.DoesNotExist:
            return Response(
                {"error": "Reservation not found"},
                status=status.HTTP_404_NOT_FOUND
            )
