from bs4 import BeautifulSoup

from rest_framework.response import Response
from rest_framework.views import APIView

from Parser.LandingParser import LandingParser
from Parser.PDFParser import PDFParser

ALLOWED_REGIONS = ('UA', 'RU', 'EN', 'US')
DEFAULT_REGION = 'UA'


class ParserMixin(APIView):
    text_message = None

    def get(self, request):
        return Response(self.text_message)

    def post(self, request):
        data = request.data
        region = self.get_region(request)

        print(region)

        if data.get('html', False):
            contact_data = LandingParser(data['html']).get_contact_data(region)

        elif data.get('url', False) and isinstance(data['url'], str) and data['url'].find('.pdf') != -1:
            contact_data = PDFParser.from_url(data['url']).get_contact_data(region)

        elif data.get('url', False) and isinstance(data['url'], str):
            contact_data = LandingParser.from_url(data['url']).get_contact_data(region)

        else:
            return Response("input correct data")

        return Response(contact_data)

    @staticmethod
    def get_region(request):

        if request.POST.get('domain'):
            return [i for i in request.POST.get('domain').split('.') if i in ALLOWED_REGIONS][0].upper()

        elif request.POST.get('html'):
            soup = BeautifulSoup(request.POST.get('html'))
            region = soup.html.attrs.get('lang').upper() if soup.html.attrs.get('lang') else DEFAULT_REGION

            if region in ALLOWED_REGIONS:
                return region
            return DEFAULT_REGION

        else:
            return DEFAULT_REGION
