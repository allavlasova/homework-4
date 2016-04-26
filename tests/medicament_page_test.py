# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from pages.medicament_page import MedicamentPage

from selenium.webdriver import DesiredCapabilities, Remote

class MedicamentPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = MedicamentPage(self.driver)
        self.page.open()

    def test_contraindications(self):
        contraindication = u'ВИЗАРСИН при беременности: Противопоказан'
        self.page.contraindication.get_contraindications(contraindication)

    def test_buy(self):
        self.page.contraindication.to_order()
        self.page.contraindication.selected_type(1)
        self.page.contraindication.increment()
        self.page.contraindication.do_order()
        self.page.wait_for_another_page()
        self.assertTrue(self.page.contraindication.check_basket())

    def test_bay_increment(self):
        self.page.contraindication.to_order()
        self.page.contraindication.selected_type(1)
        self.page.contraindication.increment()
        self.page.contraindication.increment()
        self.page.contraindication.do_order()
        self.page.wait_for_another_page()

    def test_bay_decrement(self):
        self.page.contraindication.to_order()
        self.page.contraindication.selected_type(1)
        self.page.contraindication.increment()
        self.page.contraindication.increment()
        self.page.contraindication.decrement()
        self.page.contraindication.do_order()
        self.page.wait_for_another_page()

    def tearDown(self):
        self.page.close()
        self.driver.quit()