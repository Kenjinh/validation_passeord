import pytest
from app.app import create_app


@pytest.fixture(scope="module")
def app(): 
    return create_app()