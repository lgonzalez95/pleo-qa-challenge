import pytest
from flask import url_for

@pytest.mark.options(debug=False)
def test_app(app):
  assert not app.debug, 'Ensure the app not in debug mode'

def test_test_index_response(client):
    assert client.get(url_for('index')).status_code == 200

def test_validate_response_when_value_is_12000_25(client):
    expected_response = "12 000.25"
    test_value = "12000.25"

    response = client.get(url_for(f"index"), query_string = {'money' : test_value})

    assert bytes(expected_response, 'utf-8') in response.data

def test_validate_response_when_value_is_wrong(client):
    expected_response = "{wrong value}"
    test_value = "asdas"

    response = client.get(url_for(f"index"), query_string = {'money' : test_value})

    assert bytes(expected_response, 'utf-8') in response.data


