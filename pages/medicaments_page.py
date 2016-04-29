# -*- coding: utf-8 -*-
__author__ = 'alla'
from pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class MedicamentsPage(Page):
    PATH = '/drug/'

    @property
    def search_form(self):
        return SearchForm(self.driver)

    @property
    def leaders_of_sells(self):
        return LeadersOfSells(self.driver)

    @property
    def classification(self):
        return Classification(self.driver)



class Classification(Component):
    TITLE = '//h1[@class="page-info__title"]'

    def to_link(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT,text)))
        self.driver.find_element_by_link_text(text).click()

    def get_title(self):
        title = self.driver.find_element_by_xpath(self.TITLE)
        return title.text

class LeadersOfSells(Component):
    ALL_ITEMS = "//div[@class='columns columns_percent']"
    ITEMS = "//div[@class='entry entry_medicament margin_bottom_30']//a[@class='entry__link link-holder']"
    TITLE = '//h1[@class="page-info__title"]'

    def list_leaders_of_sells(self):
        items = self.driver.find_element_by_xpath(self.ALL_ITEMS).find_elements_by_xpath(self.ITEMS)
        return items

    def get_drags_name(self, n):
        return self.list_leaders_of_sells()[n].text

    def go_to_drugs_page(self, title):
        self.driver.find_element_by_link_text(title).click()

    def result_drag(self):
        result = self.driver.find_element_by_xpath(self.TITLE)
        return result.text.split(',')[0]


class SearchForm(Component):
    INPUT_FIELD = "input.input__field.js-suggest__input"
    SUBMIT_BUTTON = '//span[@class="button__inner"]'
    ITEMS = '//div[contains(@class,"column__air")]'
    ITEM = '//div[contains(@class,"entry_medicament")]'

    def search_medicament(self, text):
        self.driver.find_element_by_css_selector(self.INPUT_FIELD).send_keys(text)

    def submit(self):
        WebDriverWait(self.driver, 50).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.SUBMIT_BUTTON))
        )
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def is_present(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                expected_conditions.presence_of_element_located((By.XPATH, self.ITEMS))
            )
            return True
        except TimeoutException:
            return False

    def items_titles(self):
        items = self.items()
        return [item.text.split(',')[0] for item in items]

    def is_empty(self):
        items = self.items()
        if len(items) == 0:
            return True
        else:
            return False

    def items(self):
        self.is_present()
        return self.driver.find_element_by_xpath(self.ITEMS).find_elements_by_xpath(self.ITEM)








