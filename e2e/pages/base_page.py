"""
BasePage defines common pages methods
"""


# page actions
class BasePage:
    def __init__(self, page: object, base_url: str) -> None:
        self.page = page
        self.base_url = base_url

    def go_to(self, url: str) -> None:
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

