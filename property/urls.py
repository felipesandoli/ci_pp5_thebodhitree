from django.urls import path
from . import views

urlpatterns = [
    path('<int:property_id>/', views.property_details, name='property_details'),
    path('all_properties/', views.all_properties, name='all_properties'),
]
