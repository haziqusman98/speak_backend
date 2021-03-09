from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sign
from .serializers import SignSerializer

@api_view(['GET'])
def get_signs(request):
    text = request.GET['text']
    signs=[]
    if text:
        for char in text:
            signs.append(SignSerializer(Sign.objects.filter(character__iexact=char).first()).data)
        return Response(signs)
    else:
        return Response("Invalid request!")