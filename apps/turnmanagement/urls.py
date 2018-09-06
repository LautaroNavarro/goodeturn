
from django.urls import path
from apps.turnmanagement.views import (create_event , view_event)

urlpatterns = [
    path('create_event/', create_event),
    path('view_event/', view_event),
]
