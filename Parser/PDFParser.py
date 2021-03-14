from PyPDF4.pdf import PdfFileReader
import requests
from io import BytesIO

from Parser.BaseParser import BaseParser


class PDFParser(BaseParser):
    def __init__(self, file):
        reader = PdfFileReader(file)

        if reader.isEncrypted:
            reader.decrypt('')

        self._reader = reader

    def get_list_of_groupd_first_last_names(self):
        pass

    def get_list_of_links_to_images(self):
        pass

    def get_list_of_phone_numbers(self, region=None):
        pass

    def get_list_of_emails(self):
        pass

    @staticmethod
    def from_url(url):
        super(PDFParser, PDFParser).from_url(url)
        request = requests.get(url)
        file = BytesIO(request.content)
        return PDFParser(file)
