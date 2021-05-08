from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import get_signs,get_gloss,verify_blob

urlpatterns = [
    path('signs', get_signs),
    path('gloss',get_gloss),
    path('verify',verify_blob),
]
urlpatterns = format_suffix_patterns(urlpatterns)