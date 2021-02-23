# from django.shortcuts import render

# import requests
from django.http import HttpResponse, HttpResponseServerError

# def IndexView(request):
# 	return HttpResponse("iosdjafiosajfio")

from rest_framework import views
from rest_framework.response import Response
from .serializers import ParseSerializer
import json
class IndexView(views.APIView):
	def get(self, request):
		yourdata= [{"url": 'url1', "html": 'http1'}, {"url": 'url2', "html": 'http2'}]
		results = ParseSerializer(yourdata, many=True).data
		return Response(results)
	
	def post(self, request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		print(body)
		return Response(request.path)