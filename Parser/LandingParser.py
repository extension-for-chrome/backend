from Parser.BaseParser import BaseParser


class LandingParser(BaseParser):

    def __init__(self, html_code):
        super().__init__(html_code)

    def get_list_of_group_first_last_names(self):
        super().get_list_of_group_first_last_names()

    def get_list_of_links_to_images(self):
        super(LandingParser, self).get_list_of_links_to_images()
