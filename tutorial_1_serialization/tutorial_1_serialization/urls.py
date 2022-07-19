from re import U
from django.urls import path, include

urlpatterns = [
    path('', include('snippets.urls')),
]