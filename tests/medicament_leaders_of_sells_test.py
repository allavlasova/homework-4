# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from pages.medicaments_page import MedicamentsPage

from selenium.webdriver import DesiredCapabilities, Remote

class MedicamentsTestLeadersOfSellsTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = MedicamentsPage(self.driver)
        self.page.open()
        self.list = self.page.leaders_of_sells

    def test_select_one_from_list(self):
        drug = self.list.get_drags_name(2)
        self.list.go_to_drugs_page(drug)
        self.page.wait_for_another_page()
        self.assertEquals(drug, self.list.result_drag())
        self.driver.back()
        drug = self.list.get_drags_name(4)
        self.list.go_to_drugs_page(drug)
        self.page.wait_for_another_page()
        self.assertEquals(drug, self.list.result_drag())


    def tearDown(self):
        self.page.close()
        self.driver.quit()