from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sign

@api_view(['GET'])
def get_signs(request):
    text = request.data.get('text',None)
    signs=[]
    if text is not None:
        for char in text:
            signs.append(Sign.objects.get(character=char))
        return Response(signs)


