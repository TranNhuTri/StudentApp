from .views import home_view, about_view, contact_view
from django.urls import path

urlpatterns = [
    path('', home_view),
    path('about', about_view),
    path('contact', contact_view)
]