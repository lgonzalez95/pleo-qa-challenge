from e2e.pages import HomePage
from e2e.settings import BASE_URL
from playwright.sync_api import Page

def test_home_page_initial_design(page: Page):
    home_page = HomePage(page, BASE_URL)

    home_page.go_to()

    expected_values = {
        "page_title": "Money Formatter",
        "h1": "Money Formatter 2021",
        "h2": "If the value is not parse properly the system returns: {wrong value}",
        "message": "The formatted value is: {wrong value}",
        "submit":"Format",
        "submit_type":"submit"
    }

    assert home_page.get_title_text() == expected_values["h1"]
    assert home_page.get_sub_title_text() == expected_values["h2"]
    assert home_page.get_message_text() == expected_values["message"]
    assert home_page.get_submit_text() == expected_values["submit"]
    assert home_page.get_submit_type() == expected_values["submit_type"]

    assert home_page.get_title() == expected_values["page_title"]


def test_wrong_text_format(page):
    home_page = HomePage(page, BASE_URL)
    home_page.go_to()

    home_page.format_text("wrong_text")
    
    # validate url and returned value
    assert "?money=" in home_page.get_url()
    assert home_page.get_result_text() == "{wrong value}"

def test_correct_int_text_format(page):
    home_page = HomePage(page, BASE_URL)
    home_page.go_to()

    home_page.format_text("112321312")
    
    # validate url and returned value
    assert "?money=" in home_page.get_url()
    assert home_page.get_result_text() == "112 321 312.00"


def test_correct_decimal_text_format(page):
    home_page = HomePage(page, BASE_URL)
    home_page.go_to()
    home_page.format_text("112321312.23")
    
    # validate url and returned value
    assert "?money=" in home_page.get_url()
    assert home_page.get_result_text() == "112 321 312.23"

def test_mandatory_fields(page):
    home_page = HomePage(page, BASE_URL)
    home_page.go_to()
    home_page.format_text("")
    
    # validate url and returned value
    assert home_page.get_result_text() == "{wrong value}"
    assert not "?money=" in home_page.get_url()

