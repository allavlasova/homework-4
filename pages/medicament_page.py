# -*- coding: utf-8 -*-
__author__ = 'alla'
from pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import requests
from urlparse import urljoin


class MedicamentPage(Page):
    COUNTER = ".amount.margin_right_10"
    ORDER_BUTTON = "//div[text()='Заказать']"
    DO_ORDER_BUTTON = "//div[text()='Оформить заказ']"
    TYPE_MENU = "//div[@class='dropdown__inner dropdown__inner_dark dropdown__inner_collapse']/div[@class='dropdown__item dropdown__item_good js-cart_add'][%s]/span/span[@class='dropdown__item__label table__cell']"
    BUY_COUNT = "//input[@class='amount__item__input js-buy_count']"
    PLUS = "//span[text()='+']"
    MINUS = "//span[text()='-']"
    RESULT_TYPE = '//div[@class = "entry entry_medicament"]//div[@class="entry__name"]'

    def __init__(self, driver, drugs_name):
        Page.__init__(self, driver)
        self.PATH = urljoin(self.BASE_URL, '/drug/')
        self.PATH = urljoin(self.PATH, drugs_name)

    def counter_is_visible(self):
        return self.driver.find_element_by_css_selector(self.COUNTER).is_displayed()

    def to_order(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.ORDER_BUTTON))
        )
        self.driver.find_element_by_xpath(self.ORDER_BUTTON).click()

    def selected_type(self, n):
        type = self.driver.find_element_by_xpath(self.TYPE_MENU % n).text
        self.driver.find_element_by_xpath(self.TYPE_MENU % n).click()
        return type

    def increment(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PLUS))
        )
        self.driver.find_element_by_xpath(self.PLUS).click()

    def decrement(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.MINUS))
        )
        self.driver.find_element_by_xpath(self.MINUS).click()

    def do_order(self):
        self.driver.find_element_by_xpath(self.DO_ORDER_BUTTON).click()

    def get_number_in_basket(self):
        number = self.driver.find_element_by_xpath(self.BUY_COUNT).get_attribute('value')
        return number

    def get_number(self):
        number = self.driver.find_element_by_xpath(self.BUY_COUNT).get_attribute('value')
        return number

    def result_type(self):
        type = self.driver.find_element_by_xpath(self.RESULT_TYPE).text
        return type

    @property
    def contraindication(self):
        return Contraindications(self.driver)

    @property
    def social_networks(self):
        return Social_networks(self.driver)

    @property
    def instructions(self):
        return Instructions(self.driver)

    @property
    def analogs(self):
        return Analog(self.driver)


class Contraindications(Component):
    ICON = "//a[contains(@class, 'icon icon_medicament')]"

    def items(self):
        return self.driver.find_elements_by_xpath(self.ICON)

    def check_links(self):
        list = self.items()
        for i in list:
            link = i.get_attribute('href')
            if requests.get(link).status_code != 200:
                return False
        return True

class Instructions(Component):
    def items(self):
        return self.driver.find_elements_by_css_selector('.catalog__item.catalog__item_pseudo.catalog__item_pseudo_dotted')

    def check_links(self):
        list = self.items()
        for i in list:
            link = i.get_attribute('href')
            if requests.get(link).status_code != 200:
                return False
        return True

class Analog(Component):
    ALL_ITEMS = "//div[@class='columns columns_percent']"
    ITEMS = "//div[@class='entry entry_medicament margin_bottom_30']//a[@class='entry__link link-holder']"
    TITLE = '//h1[@class="page-info__title"]'

    def items(self):
        items = self.driver.find_element_by_xpath(self.ALL_ITEMS).find_elements_by_xpath(self.ITEMS)
        return items

    def get_drags_name(self, n):
        result = self.items()[n].text
        return result

    def go_to_drugs_page(self, title):
        self.driver.find_element_by_link_text(title).click()

    def result_drag(self):
        result = self.driver.find_element_by_xpath(self.TITLE)
        return result.text

class Social_networks(Component):
    ICON = "//a[contains(@class, 'article__share')]"

    def items(self):
        return self.driver.find_elements_by_xpath(self.ICON)

    def check_links(self):
        list = self.items()
        for i in list:
            link = i.get_attribute('href')
            if requests.get(link).status_code != 200:
                return False
        return True

