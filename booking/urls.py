from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:property_id>/', views.booking, name='booking',
    ),
    path(
        '', views.booking, name='booking',
    ),
]
