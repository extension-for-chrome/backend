# from django.shortcuts import render

# import requests
from django.http import HttpResponse

# def IndexView(request):
# 	return HttpResponse("iosdjafiosajfio")

from rest_framework import views
from rest_framework.response import Response
from .serializers import ParseSerializer
class IndexView(views.APIView):
    def get(self, request):
        yourdata= [{"url": 'url1', "html": 'http1'}, {"url": 'url2', "html": 'http2'}]
        results = ParseSerializer(yourdata, many=True).data
        return Response(results)