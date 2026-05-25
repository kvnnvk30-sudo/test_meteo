import requests
import pytest


@pytest.fixture(scope="session")
def client():
    session = requests.Session()
    session.base_url="https://api.open-meteo.com"
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()
