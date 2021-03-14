from django.http import HttpResponse, HttpResponseServerError
from rest_framework import views
from rest_framework.response import Response
import json
import requests
import logging
from bs4 import BeautifulSoup

from Parser.PDFParser import PDFParser
from Parser.LandingParser import LandingParser


logger = logging.getLogger(__name__)


class IndexView(views.APIView):
	def get(self, request):
		logger.debug("GET request received")
		return Response({
			"url": "https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/pdf_reference_archives/PDFReference.pdf"
		})

	def post(self, request):
		logger.debug("POST request received")
		json_string = request.body.decode('utf-8').replace("\n", " ")

		try:
			data = json.loads(json_string)
		except json.decoder.JSONDecodeError:
			err_message = f"unreadable json: '{json_string}'"
			logger.error(err_message)
			return Response({"error message": err_message})

		if not isinstance(data, dict):
			return Response(request.path)

		url = data.get('url')
		html = data.get('html')

		if html is not None:
			parser = LandingParser(html)

		elif isinstance(url, str):
			parser = PDFParser.from_url(url) if url.endswith('.pdf') else LandingParser.from_url(url)

		else:
			return Response(request.path)

		return Response(request.path)
