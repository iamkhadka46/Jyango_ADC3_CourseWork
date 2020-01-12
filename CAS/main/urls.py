from django.urls import path, include
from . import views
from django.contrib import admin
from main.views import LoginView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
 
    path('', views.home_view, name="home"),
    path('signup/', views.signup_view, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('search/', views.search, name = "search"),
    path('assignments/', views.assignment_list, name = "assignment_list"),
    path('assignments/upload/', views.upload_assignment, name = "upload_assignment"),
    path('assignments/<int:pk>/', views.delete_book, name='delete_assignment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    