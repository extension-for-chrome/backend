# from django.shortcuts import render

# import requests
from django.http import HttpResponse, HttpResponseServerError

# def IndexView(request):
# 	return HttpResponse("iosdjafiosajfio")

from rest_framework import views
from rest_framework.response import Response
from .serializers import ParseSerializer
import json
import requests
import re
import glob
import logging

logger = logging.getLogger(__name__)

class IndexView(views.APIView):
	def get(self, request):
		logger.error("get request received")
		print(__name__)
		yourdata= [{"url": 'url1', "html": 'http1'}, {"url": 'url2', "html": 'http2'}]
		results = ParseSerializer(yourdata, many=True).data
		return Response(results)
		
	
	def post(self, request):
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		url = body['url']
		html_data = body['html']
		print(f'url: {url}')
		print(f'html data: {html_data}')

		#https://lpnu.ua/
		req = requests.get(url)

		src = req.text
		phone = getPhone(src)
		print(f'phone: {phone}')
		return Response(request.path)

def getPhone(string):
	phone = ''
	phoneRegEx = re.compile('\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4}|\d{2})(?: *x(\d+))?\s*')
	m = phoneRegEx.search(string)
	
	return m