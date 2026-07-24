import responses
import requests
import pytest

@pytest.mark.api
def test_httpbin_json(base_url):
    resp = requests.get(f"{base_url}/json")
    assert resp.status_code == 200
    assert "slideshow" in resp.json()

@pytest.mark.api
@responses.activate
def test_user_mock():
    responses.add(responses.GET, "https://api.example.com/user/1", json={"id": 1, "name": "mock-user"}, status=200)
    resp = requests.get("https://api.example.com/user/1")
    assert resp.json()["name"] == "mock-user"
