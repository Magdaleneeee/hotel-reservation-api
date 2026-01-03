from django.db import models

class Room(models.Model):
    ROOM_TYPES = [
        ('SINGLE', 'Single'),
        ('DELUXE', 'Deluxe'),
        ('SUITE', 'Suite'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)  # 👈 NEW FIELD

    def __str__(self):
        return f"Room {self.room_number}"
