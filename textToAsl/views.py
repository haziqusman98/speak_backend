from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sign
from .serializers import SignSerializer
from .apps import TexttoaslConfig
import cv2

def verify_blob(vid):
    if vid is not None:
        with open("temp.mp4", "wb") as vid_writer:
            vid_stream = vid.read()
            vid_writer.write(vid_stream)
        try:
            vidcap = cv2.VideoCapture("temp.mp4")
            return vidcap.read()[0]
        except:
            return False
    else:
        return False

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
    vid = request.FILES.get("vid",None)
    return Response(verify_blob(vid))
    # if verify_blob(vid):
    #     return Response({"gloss":TexttoaslConfig.predictor.predict(vid)})
    # else:
    #     return Response("Invalid blob")
    