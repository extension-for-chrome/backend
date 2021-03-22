from PyPDF4.pdf import PdfFileReader
import requests
import phonenumbers
import re
from io import BytesIO

from parser.BaseParser import BaseParser


class PDFParser(BaseParser):
    def __init__(self, file):
        reader = PdfFileReader(file)

        if reader.isEncrypted:
            reader.decrypt('')

        num_pages = reader.numPages

        if num_pages < 6:
            pages_index = list(range(num_pages))

        else:
            pages_index = list(range(3)) + list(range(num_pages - 4, num_pages - 1))

        print(pages_index)
        self.pages_index = pages_index
        self._reader = reader

    def get_list_of_group_first_last_names(self):
        pass

    def get_list_of_links_to_images(self):
        pass

    def get_list_of_phone_numbers(self, region=None):

        return [
            phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
            for page_index in self.pages_index
            for match in phonenumbers.PhoneNumberMatcher(
                self._reader.getPage(page_index).extractText(),
                region
            )
        ]

    def get_list_of_emails(self):

        emails = list()
        for page_index in self.pages_index:
            page_text = self._reader.getPage(page_index).extractText()
            emails.extend(re.findall(r'[\w\.]+@[\w-]+\.*[\w-]*\.[\w-]{2,4}', page_text))

        return emails

    @staticmethod
    def from_url(url):
        super(PDFParser, PDFParser).from_url(url)
        request = requests.get(url)
        file = BytesIO(request.content)
        return PDFParser(file)
