from django.urls import path
from django.views.generic import TemplateView  # Import TemplateView
from django.contrib.auth.views import LogoutView
from .views import home_view
urlpatterns = [
  path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
   path('home/', home_view , name='home'),
     path('logout/', LogoutView.as_view(), name='logout'),
   
 # Use TemplateView to render login.html
    # Other app-specific URLs...
]
