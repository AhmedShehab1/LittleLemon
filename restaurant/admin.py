from django.contrib import admin
from .models import Menu, Booking
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')
    search_fields = ('title', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests')
    search_fields = ('name', 'date')
    list_filter = ('date',)
