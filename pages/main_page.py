# -*- coding: utf-8 -*-
__author__ = 'alla'
from selenium.webdriver.support.ui import WebDriverWait
from urlparse import urljoin
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
class Page:
    BASE_URL = 'https://health.mail.ru/'
    PATH = ''
    HDR_XPATH = ''

    def __init__(self, driver):
        self.driver = driver
        self.window_handle = driver.current_window_handle

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
        self.wait_page()

    def wait_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                 expected_conditions.presence_of_element_located((By.XPATH, self.HDR_XPATH))
            )
        except TimeoutException:
            print "No header found"

    def close(self):
        self.driver.close()


class Component(object):
    def __init__(self, driver):
        self.driver = driver