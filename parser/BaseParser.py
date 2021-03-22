from abc import ABC, abstractmethod


class BaseParser(ABC):
    @abstractmethod
    def get_list_of_group_first_last_names(self):
        pass

    @abstractmethod
    def get_list_of_links_to_images(self):
        pass

    @abstractmethod
    def get_list_of_phone_numbers(self, region='ua'):
        pass

    @abstractmethod
    def get_list_of_emails(self):
        pass

    def get_contact_data(self, region='UA'):
        return {
            "phone number": self.get_list_of_phone_numbers(region),
            "email": self.get_list_of_emails()
        }

    @staticmethod
    @abstractmethod
    def from_url(url):
        if not isinstance(url, str):
            raise TypeError('url must be string')
