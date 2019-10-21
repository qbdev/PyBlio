"""Testing module for the Unit Test on the base app and classes"""
import pytest
from core.app import app


@pytest.fixture
def client():
    """Init the Flask app for testing"""
    app.config['TESTING'] = True
    clientapp = app.test_client()
    yield clientapp


def test_home_status(client):
    """Test the existence and basic behaviour of the app"
    by sending a GET request to / and check the status code"""
    result = client.get('/')
    assert result.status_code == 200
