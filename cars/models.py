from django.conf import settings
from django.db import models

class Car(models.Model):
    STATUS_CHOICES = [
        ('rent', 'ქირავდება'),
        ('sale', 'იყიდება'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
