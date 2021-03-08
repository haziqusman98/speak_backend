from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_signs

urlpatterns = [
    path('signs', get_signs),
]
urlpatterns = format_suffix_patterns(urlpatterns)