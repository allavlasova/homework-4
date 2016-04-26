# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from pages.medicaments_page import MedicamentsPage

from selenium.webdriver import DesiredCapabilities, Remote


class MedicamentsClassificationTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = MedicamentsPage(self.driver)
        self.page.open()
        self.classification_list = self.page.classification

    def test_drug_type_selection(self):
        text = u"Витамины"
        self.classification_list.go_to(text)
        self.page.wait_for_another_page()
        self.assertEquals(text, self.classification_list.get_title())
        self.driver.back()
        text = u"Миорелаксанты"
        self.classification_list.go_to(text)
        self.page.wait_for_another_page()
        self.assertEquals(text, self.classification_list.get_title())


    def tearDown(self):
        self.page.close()
        self.driver.quit()
