from bs4 import BeautifulSoup
from helium import *

class Scraper():

    def scrape_data(self, url):
        browser = start_chrome(url, headless=True)
        source = browser.page_source
        print(source)
        # session = BeautifulSoup(source, 'lxml')
        # question = session.find_all("div", {"class": "q-text puppeteer_test_question_title"})
        # print(question)

scraper = Scraper()
scraper.scrape_data('https://pl.quora.com/Do-os%C3%B3b-kt%C3%B3re-by%C5%82y-w-Australii-co-was-najbardziej-zaskoczy%C5%82o')