from django.urls import path
from .views import get_all_posts

urlpatterns = [
    path("", get_all_posts)
]
