import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import urls
from .services import ParserMixin

logger = logging.getLogger(__name__)


@api_view(['GET'])
def api_root(request):
	app_name = urls.app_name

	return Response({
		url.name: reverse(f'{app_name}:{url.name}', request=request)
		for url_num, url in enumerate(urls.urlpatterns) if url_num > 0
	})


class Parse(ParserMixin):
	text_message = 'Parser'
