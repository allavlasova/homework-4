# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from pages.medicament_page import MedicamentPage

from selenium.webdriver import DesiredCapabilities, Remote

class MedicamentsTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = MedicamentPage(self.driver)
        self.page.open()

    def test_search(self):
        query = u'ВИЗАРСИН, таблетки'
        self.page.search_form.search_medicament(query)
        self.page.search_form.submit()
        list = self.page.resultlist
        suggested_titles = list.items_titles()
        self.assertIn(query, suggested_titles)



    def tearDown(self):
        self.page.close()
        self.driver.quit()