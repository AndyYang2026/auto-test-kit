import pytest

@pytest.mark.ui
def test_open_example(page):
    page.goto("https://example.com")
    assert "Example" in page.title()
