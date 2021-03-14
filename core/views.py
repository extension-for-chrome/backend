from django.http import HttpResponse, HttpResponseServerError
from rest_framework import views
from rest_framework.response import Response
from .serializers import ParseSerializer
import json
import requests
import re
import glob
import logging
import phonenumbers
from bs4 import BeautifulSoup

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
		req = requests.get(url)

		src = req.text
		soup = BeautifulSoup(src)
		x = phonenumbers.parse(soup.find("div", class_="col-sm-4").text, None)
		print(x)
		return Response(request.path)
