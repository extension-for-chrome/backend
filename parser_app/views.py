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
from .MyClass import MyClass

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
		url = body[0]['url']
		html_data = body[0]['html']
		req = requests.get(url)

		src = req.text
		parser = MyClass(src)
		number_list = parser.get_list_of_phone_numbers()
		#print(parser.get_list_of_phone_numbers())
		email_list = parser.get_list_of_emails()

		data = {
			"phone numbers": number_list,
			"emails": email_list
		}
		res = json.dumps(data, indent=4)
		print(res)
		return Response(res)