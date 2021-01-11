

# page locators
btn_submit = '#submit'
h1_title= 'h1'
h2_title= 'h2'
lbl_result = "#result"
lbl_message = '.result-message'
txt_money = "#money"

# page actions
class HomePage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    # wrappers
    def go_to(self):
        self.page.goto(self.base_url)

    def format_text(self, money_text) -> None:
        self.page.type(txt_money, money_text)
        self.click_submit()

    # single element attributes/actions
    def click_submit(self) -> None:
        self.page.click(btn_submit)

    def get_title_text(self) -> None:
        return self.page.innerText(h1_title)
    
    def get_sub_title_text(self) -> None:
        return self.page.innerText(h2_title)

    def get_message_text(self) -> None:
        return self.page.innerText(lbl_message)

    def get_submit_type(self) -> None:
        return self.page.getAttribute(btn_submit, "type")

    def get_result_text(self) -> None:
        return self.page.innerText(lbl_result)

    def get_submit_text(self) -> None:
        return self.page.innerText(btn_submit)

        

