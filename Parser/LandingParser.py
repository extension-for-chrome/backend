from Parser.BaseParser import BaseParser
import requests
import phonenumbers
import re


class LandingParser(BaseParser):
    def __init__(self, html_code):
        self._html = html_code

    def get_list_of_group_first_last_names(self):
        pass

    def get_list_of_links_to_images(self):
        pass

    def get_list_of_phone_numbers(self, region='GB'):
        return [
            phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
            for match in phonenumbers.PhoneNumberMatcher(self._html, region)
        ]

    def get_list_of_emails(self):
        return re.findall(r'[\w\.]+@[\w-]+\.*[\w-]*\.[\w-]{2,4}', self._html)

    @staticmethod
    def from_url(url):
        super(LandingParser, LandingParser).from_url(url)
        html = requests.get(url).text
        return LandingParser(html)
