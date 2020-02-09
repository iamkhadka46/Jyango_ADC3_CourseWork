from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.api_data, name="api_data"),
    path('courses/<int:pk>/', views.update_api_data, name = "update_api_data"),
    path('api/assignments/<int:PAGENO>/<int:SIZE>', views.api_assignments, name="api_assignments_data"), 
    path('api/posts/<int:PAGENO>/<int:SIZE>', views.api_posts, name="api_posts_data"),
    path('courses/create/', views.create_course, name = "create_course"),
]