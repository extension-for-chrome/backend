from parser.BaseParser import BaseParser
import requests
import phonenumbers
import re
import pathlib


class LandingParser(BaseParser):
    def __init__(self, url, html_code):
        self.url = url
        self._html = html_code

    def get_list_of_group_first_last_names(self):
        return list()

    def get_list_of_links_to_images(self):
        pass

    def get_list_of_phone_numbers(self, region='UA'):
        return list({
            phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
            for match in phonenumbers.PhoneNumberMatcher(self._html, region)
        })

    def get_list_of_emails(self):
        return list({
            email
            for email in re.findall(r'[\w\.]+@[\w-]+\.*[\w-]*\.[\w-]{2,4}', self._html)
            if pathlib.Path(email).suffix not in ['png', 'jped', 'svg']
        })

    @staticmethod
    def from_url(url):
        super(LandingParser, LandingParser).from_url(url)
        html = requests.get(url).text
        return LandingParser(url, html)
