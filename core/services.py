from rest_framework.response import Response
from rest_framework.views import APIView

from Parser.LandingParser import LandingParser
from Parser.PDFParser import PDFParser


class ParserMixin(APIView):
    text_message = None

    def get(self, request):
        return Response(self.text_message)

    @staticmethod
    def post(request):
        data = request.data

        if data.get('html', False):
            contact_data = LandingParser(data['html']).get_contact_data()

        elif data.get('url', False) and isinstance(data['url'], str) and data['url'].find('.pdf') != -1:
            contact_data = PDFParser.from_url(data['url']).get_contact_data()

        elif data.get('url', False) and isinstance(data['url'], str):
            contact_data = LandingParser.from_url(data['url']).get_contact_data()

        else:
            return Response("input correct data")

        return Response(contact_data)
