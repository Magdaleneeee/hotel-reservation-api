# Hotel Reservation API

This is a backend API for a hotel reservation system built with Django and Django REST Framework.

The API manages hotel rooms and reservations, allowing users to view available rooms, create reservations, view their bookings, and cancel reservations. This project was built as a capstone project for the ALX Back-End Web Development program.

---

## Features

- List and create hotel rooms
- Filter rooms by capacity
- Create reservations
- View reservations for the authenticated user
- Cancel reservations
- Room availability tracking
- Django admin panel for managing rooms and reservations

---

## API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| GET, POST | `/api/rooms/` | List or create rooms |
| GET | `/api/rooms/?capacity=2` | Filter rooms by capacity |
| GET, POST | `/api/reservations/` | View or create reservations (authenticated users only) |
| POST | `/api/reservations/<id>/cancel/` | Cancel a reservation |

---

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (default Django development database)
