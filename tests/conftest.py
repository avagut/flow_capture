"""Common fixtures to all tests."""
import pytest
from src import app as _app
from src import create_app

@pytest.fixture
def app():
    yield _app
