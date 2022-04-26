from django.contrib import admin
from .models import Room, Message

# Register your models here.
# This shows the models in Django Admin Panel
admin.site.register(Room)
admin.site.register(Message)
