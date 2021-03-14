from rest_framework.response import Response
from rest_framework.views import APIView

from Parser.LandingParser import LandingParser


def parse_html(html):

    parser = LandingParser(html)
    return {
        'list_emails': parser.get_list_of_emails(),
        'phones_numbers': parser.get_list_of_phone_numbers(region='GB')
    }


class ParserMixin(APIView):
    text_message = None

    def get(self, request):
        return Response(self.text_message)

    @staticmethod
    def post(request):
        if request.POST.get('html'):
            data = parse_html(request.POST.get('html'))
            return Response(data)
        return Response('You should add html text')
