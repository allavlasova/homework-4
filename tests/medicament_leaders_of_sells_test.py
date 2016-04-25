# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from pages.medicament_page import MedicamentPage

from selenium.webdriver import DesiredCapabilities, Remote

class MedicamentsTestLeadersOfSells(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = MedicamentPage(self.driver)
        self.page.open()
        self.list = self.page.leaders_of_sells

    def test_select_one_from_list(self):
        title = u'РЕДУКСИН'
        self.list.get_drug_from_leaders_of_sells(title)
        self.page.wait_for_another_page()
        self.assertEquals(title, self.list.get_title())
        self.driver.back()
        title = u'ФЛУОКСЕТИН'
        self.list.get_drug_from_leaders_of_sells(title)
        self.page.wait_for_another_page()
        self.assertEquals(title, self.list.get_title())

    def tearDown(self):
        self.page.close()
        self.driver.quit()