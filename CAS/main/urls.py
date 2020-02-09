from django.urls import path, include
from . import views
from django.contrib import admin
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
    path('assignments/<int:pk>/', views.delete_assignment, name='delete_assignment'),
    path('submissions/', views.submission_list, name = "submission_list"),
    path('submissions/upload/', views.upload_submission, name = "upload_submission"),
    path('submissions/<int:pk>/', views.delete_submission, name='delete_submission'),
    path('course', views.course),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.delete), 
    path('api/assignments/<int:PAGENO>/<int:SIZE>', views.api_assignments, name="api_assignments_data"), 
    path('api/posts/<int:PAGENO>/<int:SIZE>', views.api_posts, name="api_posts_data"), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    