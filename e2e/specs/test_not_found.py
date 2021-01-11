from e2e.pages import NotFoundPage
from e2e.settings import BASE_URL

def test_not_found_page_initial_design(page):
    not_found_page = NotFoundPage(page, BASE_URL)

    not_found_page.go_to()

    expected_values = {
        "page_title": "Money Formatter",
        "h1": "The requested page was not found",
        "h2": "404 Error",
    }

    assert not_found_page.get_title_text() == expected_values["h1"]
    assert not_found_page.get_sub_title_text() == expected_values["h2"]

    assert not_found_page.get_title() == expected_values["page_title"]
