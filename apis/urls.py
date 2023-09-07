from django.urls import path
from .views import RandomAPIView
urlpatterns = [
    path('',RandomAPIView.as_view())
]
