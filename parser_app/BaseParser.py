from abc import ABC, abstractmethod
import phonenumbers
import re


class BaseParser(ABC):

    @abstractmethod
    def __init__(self, html):
        self._html = html

    @abstractmethod
    def get_list_of_groupd_first_last_names(self):
        pass

    @abstractmethod
    def get_list_of_links_to_images(self):
        pass

    def get_list_of_phone_numbers(self, region=None):
        return [
            phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
            for match in phonenumbers.PhoneNumberMatcher(self._html, region)
        ]

    def get_list_of_emails(self):
        return re.findall(r'[\w\.]+@[\w-]+\.[\w-]{2,4}', self._html)