# -*- coding: utf-8 -*-
__author__ = 'alla'
from pages.main_page import Component, Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class MedicamentPage(Page):
    PATH = '/drug/vizarsin/'
    HDR_XPATH = '//span[contains(@class, "input__decorator")]'

    @property
    def contraindication(self):
        return Contraindications(self.driver)


class Contraindications(Component):

    def get_title(self):
        title = self.driver.find_element_by_xpath(self.TITLE)
        return title.text.split(',')[0]

    def get_contraindications(self, contraindication):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[@title='%s']" % contraindication ))
        )
        self.driver.find_element_by_xpath("//a[@title='%s']" % contraindication).click()

    def to_order(self):
        self.driver.find_element_by_xpath("//div[@class='dropdown__text'][text()='Заказать']").click()

    def selected_type(self, n):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='dropdown__inner dropdown__inner_dark dropdown__inner_collapse']/div/span/span[@class='dropdown__item__label table__cell'][%s]" % n))
        )
        self.driver.find_element_by_xpath("//div[@class='dropdown__inner dropdown__inner_dark dropdown__inner_collapse']/div/span/span[@class='dropdown__item__label table__cell'][%s]" % n).click()


    def increment(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[@class='amount__item amount__item_changer amount__item_plus js-buy_count_change'][text()='+']"))
        )
        self.driver.find_element_by_xpath("//span[@class='amount__item amount__item_changer amount__item_plus js-buy_count_change'][text()='+']").click()

    def decrement(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//span[@class='amount__item amount__item_changer amount__item_minus js-buy_count_change'][text()='-']"))
        )
        self.driver.find_element_by_xpath("//span[@class='amount__item amount__item_changer amount__item_minus js-buy_count_change'][text()='-']").click()

    def do_order(self):
        self.driver.find_element_by_xpath("//div[@class='button__text'][text()='Оформить заказ']").click()

    def check_basket(self):
        try:
            item = self.driver.find_element_by_xpath("//div[@class='entry entry_medicament']/div[@class='table__cell']/div[@class='entry__name']")
            return True
        except Exception as e:
            print(e)
            return False

