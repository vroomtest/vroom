import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page."""
    rv = client.get('/')
    assert b'Enter your password' in rv.data

def test_strong_password(client):
    """Test submitting a strong password."""
    rv = client.post('/', data=dict(password='StrongPass123'))
    assert b'Welcome' in rv.data

def test_weak_password(client):
    """Test submitting a weak password."""
    rv = client.post('/', data=dict(password='password'))
    assert b'Password does not meet the requirements' in rv.data
