
from e2e.pages.base_page import BasePage

# page locators
h1_title= 'h1'
h2_title= 'h2'

# page actions
class NotFoundPage(BasePage):
    def __init__(self, page, base_url):
        BasePage.__init__(self, page, base_url)

    def go_to(self) -> None:
        BasePage.go_to(self, f'{self.base_url}/wrong-page')

    
    # single element attributes/actions
    def get_title_text(self) -> str:
        return self.page.innerText(h1_title)
    
    def get_sub_title_text(self) -> str:
        return self.page.innerText(h2_title)

    

        

