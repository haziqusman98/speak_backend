from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sign
from .serializers import SignSerializer
from .apps import TexttoaslConfig
import cv2

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

@api_view(['POST'])
def get_gloss(request):
    vid = request.data.get("vid")
    return Response({"gloss":TexttoaslConfig.predictor.predict(vid)})

@api_view(['POST'])
def verify_blob(request):
    vid = request.FILES.get("vid")
    if vid is not None:
        return Response("True")
    return Response("False")

    # f = open("request.txt",'w')
    # f.write(request)
    # vidcap = cv2.VideoCapture(vid)
    