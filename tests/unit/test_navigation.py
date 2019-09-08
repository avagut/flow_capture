import pytest
from flask import Flask
from flask.blueprints import Blueprint
from src import app


def test_app_structure(client):
    """Check app structure."""
    assert isinstance(app, Flask)

def test_home_page(client):
    """Verify home page access."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"

def test_blueprints(client):
    """Check blueprint access."""
    assert 'navigation' in app.blueprints
    assert isinstance(app.blueprints['navigation'], Blueprint)
