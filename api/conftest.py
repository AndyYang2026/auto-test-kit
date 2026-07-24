import pytest
from common.config import config

@pytest.fixture(scope="session")
def base_url():
    return config.BASE_URL

@pytest.fixture(scope="session")
def api_headers():
    return {
        "Authorization": f"Bearer {config.API_TOKEN}",
        "Content-Type": "application/json",
    }
