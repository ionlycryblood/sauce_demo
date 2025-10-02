import allure
import pytest
from playwright.sync_api import sync_playwright



@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def page(request):
    browser_name = request.param
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch()
        context = browser.new_context()
        page = context.new_page()
        allure.dynamic.label("browser", browser_name)
        yield page
        browser.close()

