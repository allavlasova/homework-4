# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from pages.medicaments_page import MedicamentsPage
from selenium.webdriver import DesiredCapabilities, Remote

class MedicamentsSearchTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = MedicamentsPage(self.driver)
        self.page.open()
        self.search_form = self.page.search_form

    def test_search_for_existent_drug(self):
        query = u'ВИЗАРСИН'
        self.search_form.search_medicament(query)
        self.search_form.submit()
        self.assertFalse(self.search_form.is_empty())
        titles = self.search_form.items_titles()
        self.assertIn(query, titles)

    def test_search_by_eng(self):
        query = 'VIZARSIN'
        self.search_form.search_medicament(query)
        self.search_form.submit()
        self.assertFalse(self.search_form.is_empty())
        titles = self.search_form.items_titles()
        self.assertIn(u'ВИЗАРСИН', titles)

    def test_search_for_non_existent_drug(self):
        query = u'несуществующиетаблетки'
        self.search_form.search_medicament(query)
        self.search_form.submit()
        self.assertTrue(self.search_form.is_empty())

    def tearDown(self):
        self.page.close()
        self.driver.quit()
