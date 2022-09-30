from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright, ViewportSize
import time

def make_screenshots(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        queryselector =  page.query_selector('.q-box.qu-pt--medium')
        queryselector.screenshot(path='test.png')
        browser.close()
make_screenshots('https://pl.quora.com/Do-os%C3%B3b-kt%C3%B3re-by%C5%82y-w-Australii-co-was-najbardziej-zaskoczy%C5%82o')