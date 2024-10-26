from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=60, db_index=True)
    no_of_guests = models.SmallIntegerField()
    date = models.DateTimeField(db_index=True)
    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    def __str__(self):
        return f"{self.title} - {self.price}"
