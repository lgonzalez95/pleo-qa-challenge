

# page locators
btn_submit = '#submit'
h1_title= 'h1'
h2_title= 'h2'
lbl_result = "#result"
lbl_message = '.result-message'
txt_money = "#money"

# page actions
class BasePage:
    def __init__(self, page: object, base_url: str) -> None:
        self.page = page
        self.base_url = base_url

    def go_to(self, url: str) -> None:
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

