"""Implements tests for the app"""


def test_hello(test_app):
    """Tests if the hello endpoint is gettable"""
    response = test_app.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_env(test_app):
    """Tests if the ev endpoint is gettable"""
    response = test_app.get("/hello/env")
    assert response.status_code == 200
    assert response.json() == {"env": "testing"}
