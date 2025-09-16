from django.db import models
from django.contrib.auth import get_user_model

#get auth model
User = get_user_model()

class Car(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars",limit_choices_to={"role": "dealer"})
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class ServiceBooking(models.Model):
    SERVICE_TYPES = [
        ("maintenance", "Maintenance"),
        ("repair", "Repair"),
        ("inspection", "Inspection"),
    ]
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="services")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booked_services",limit_choices_to={"role": "customer"})
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField(blank=True, null=True)
    assigned_mechanic = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": "mechanic"},
        related_name="assigned_services"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    booked_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.service_type} - {self.car} ({self.status})"
