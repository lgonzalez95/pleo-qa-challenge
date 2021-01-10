"""
Route miscelaneous tests
"""

import pytest
from flask import url_for
import werkzeug

@pytest.mark.options(debug=False)
def test_app(app):
  assert not app.debug, 'Ensure the app not in debug mode'

def test_index_response(client):
    assert client.get(url_for('index')).status_code == 200


def test_route_not_found(client):
  # verify that if the route does not exist werkzeug 
  with pytest.raises(werkzeug.routing.BuildError):
      assert client.get(url_for('not-found'))


