from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class Scraper():

    def scrape_data(self, url):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        time.sleep(2)
        # driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
        # button_el = driver.find_elements_by_class_name('q-text qu-ellipsis qu-whiteSpace--nowrap')[0]
        # button_el.click()
        # action = webdriver.common.action_chains.ActionChains(driver)
        # action.move_to_element_with_offset(button_el, 5, 0)
        # action.click()
        # action.perform()
        source = driver.page_source
        # source = driver.execute_script("return document.body.innerHTML;")
        session = BeautifulSoup(source, 'html.parser')
        question = session.find("div", {"class": "q-text puppeteer_test_question_title"}).get_text()
        answers_divs = session.find_all("div", {"class": "q-box spacing_log_answer_content puppeteer_test_answer_content"})
        answers = [i.get_text() for i in answers_divs]
        driver.quit()
        return {"answers": answers, "question": question}
        

