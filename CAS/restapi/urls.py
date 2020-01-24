from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.api_data, name="api_data"),
    path('courses/<int:pk>/', views.update_api_data,)
]