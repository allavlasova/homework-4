# -*- coding: utf-8 -*-
__author__ = 'alla'
from pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class MedicamentPage(Page):
    PATH = '/drug/'
    HDR_XPATH = '//span[contains(@class, "input__decorator")]'

    @property
    def search_form(self):
        return SearchForm(self.driver)

    @property
    def resultlist(self):
        return ResultList(self.driver)



class SearchForm(Component):
    PATH = ''
    INPUT_FIELD = "//form[input/@class='input__field']]"
    SUBMIT_BUTTON = '//span[@class="button__inner"]'

    def search_medicament(self, text):
        self.driver.find_element_by_css_selector('input.input__field.js-suggest__input').send_keys(text)

        #wait = WebDriverWait(self.driver, 15, 10)

    def submit(self):
        WebDriverWait(self.driver, 50).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON))
        )
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()



class ResultList(Page):
    #ITEM = '.entry_medicament'
    ITEM = '//div[@class="entry_medicament"]'
    #TITLE = '.entry__name'
    #TITLE = '//div[@class="entry_medicament"]'

    def is_present(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                #expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.ITEM))
                expected_conditions.presence_of_element_located((By.XPATH, self.ITEM))
            )
            return True
        except TimeoutException:
            return False

    def items_titles(self):
        items = self.items()
        return [item.text for item in items]

    def items(self):
        self.is_present()
        return self.driver.find_elements_by_css_selector('a.entry__link.link-holder')




