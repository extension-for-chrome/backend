from abc import ABC, abstractmethod


class BaseParser(ABC):
    @abstractmethod
    def get_list_of_groupd_first_last_names(self):
        pass

    @abstractmethod
    def get_list_of_links_to_images(self):
        pass

    @abstractmethod
    def get_list_of_phone_numbers(self):
        pass

    @abstractmethod
    def get_list_of_emails(self):
        pass

    @staticmethod
    @abstractmethod
    def from_url(url):
        if not isinstance(url, str):
            raise TypeError('url must be string')
