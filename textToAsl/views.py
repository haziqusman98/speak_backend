from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sign
from .serializers import SignSerializer

@api_view(['POST'])
def get_signs(request):
    text = request.data.get('text',None)
    signs=[]
    if text is not None:
        for char in text:
            signs.append(SignSerializer(Sign.objects.filter(character__iexact=char).first()).data)
        return Response(signs)
    else:
        return Response(request)