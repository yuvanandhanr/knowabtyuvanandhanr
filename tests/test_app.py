import os
import sys
import pytest

# Ensure project root is on sys.path so tests can import app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


def test_index(client):
    r = client.get('/')
    assert r.status_code == 200
    assert b'Featured Projects' in r.data


def test_contact_get(client):
    r = client.get('/contact')
    assert r.status_code == 200
    assert b'Contact' in r.data


def test_contact_post_redirects(client):
    r = client.post('/contact', data={'name': 'A', 'email': 'a@b.com', 'message': 'hi'}, follow_redirects=True)
    assert r.status_code == 200
    assert b'Thanks for your message' in r.data
