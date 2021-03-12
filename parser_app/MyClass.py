from .BaseParser import BaseParser
from abc import ABC, abstractmethod
import phonenumbers
import re


class MyClass(BaseParser):

	def __init__(self, html):
		super(MyClass, self).__init__(html)
		self.html = html

	def get_list_of_phone_numbers(self, region=None):
		return [
            phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
            for match in phonenumbers.PhoneNumberMatcher(self._html, region)
        ]




	def get_list_of_groupd_first_last_names(self):
		pass

	def get_list_of_links_to_images(self):
		pass



	def get_list_of_emails(self):
		return re.findall(r'[\w\.]+@[\w-]+\.[\w-]{2,4}', self._html)
    