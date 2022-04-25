from django.urls import path
from .views import detail_view, create_view
urlpatterns = [
    path('create', create_view),
    path('detail', detail_view),
]