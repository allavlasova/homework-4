# -*- coding: utf-8 -*-
__author__ = 'alla'
import os
import unittest
from pages.medicament_page import MedicamentPage

from selenium.webdriver import DesiredCapabilities, Remote

class MedicamentPageTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.page = MedicamentPage(self.driver, 'vizarsin')
        self.page.open()


    def test_contraindications(self):
        self.assertTrue(self.page.contraindication.check_links())

    def test_counter(self):
        self.page.login()
        self.page.to_order()
        self.page.selected_type(1)
        self.assertEquals(1, int(self.page.get_number()))
        self.page.increment()
        self.page.increment()
        self.assertEquals(3, int(self.page.get_number()))
        self.page.decrement()
        self.assertEquals(2, int(self.page.get_number()))

    #проверка инкримента/дикримента в корзине
    def test_counter_in_basket(self):
        self.page.login()
        self.page.to_order()
        self.page.selected_type(1)
        self.page.do_order()
        self.page.wait_for_another_page()
        self.assertEquals(1, int(self.page.get_number_in_basket()))
        self.driver.back()
        self.page.increment()
        self.page.increment()
        self.page.do_order()
        self.page.wait_for_another_page()
        self.assertEquals(3, int(self.page.get_number_in_basket()))
        self.driver.back()
        self.page.decrement()
        self.page.do_order()
        self.page.wait_for_another_page()
        self.assertEquals(2, int(self.page.get_number_in_basket()))

    #проверка появление счетчика после выбора типа
    def test_counter_visible(self):
        self.assertFalse(self.page.counter_is_visible())
        self.page.to_order()
        self.page.selected_type(1)
        self.assertTrue(self.page.counter_is_visible())

     #проверка что нельзя ввести отрицательные значения
    def test_negative_counter_value(self):
        self.page.to_order()
        self.page.selected_type(1)
        self.page.decrement()
        self.assertFalse(self.page.counter_is_visible())

    #проверка соответсвия типов
    def test_drugs_type_check(self):
        self.page.login()
        self.page.to_order()
        expected_type = self.page.selected_type(3)
        self.page.do_order()
        self.page.wait_for_another_page()
        self.assertEquals(expected_type, self.page.result_type())
        self.driver.back()
        self.page.decrement()
        self.page.to_order()
        expected_type = self.page.selected_type(2)
        self.page.do_order()
        self.page.wait_for_another_page()
        self.assertEquals(expected_type, self.page.result_type())

    def test_instructions(self):
        self.assertTrue(self.page.instructions.check_links())

    def test_analogs(self):
        drug = self.page.analogs.get_drags_name(2)
        self.page.analogs.go_to_drugs_page(drug)
        self.page.wait_for_another_page()
        self.assertEquals(drug.split(',')[0], self.page.analogs.result_drag())
        self.driver.back()
        drug = self.page.analogs.get_drags_name(3)
        self.page.analogs.go_to_drugs_page(drug)
        self.page.wait_for_another_page()
        self.assertEquals(drug.split(',')[0], self.page.analogs.result_drag())

    def test_social_networks(self):
        self.assertTrue(self.page.social_networks.check_links())

    def tearDown(self):
        self.page.close()
        self.driver.quit()