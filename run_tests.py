# -*- coding: utf-8 -*-
import unittest

from tests.medicament_classification_test import MedicamentsClassificationTest
from tests.medicament_leaders_of_sells_test import MedicamentsTestLeadersOfSellsTest
from tests.medicament_page_test import MedicamentPageTest
from tests.medicament_search_test import MedicamentsSearchTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MedicamentPageTest),
        unittest.makeSuite(MedicamentsSearchTest),
        unittest.makeSuite(MedicamentsClassificationTest),
        unittest.makeSuite(MedicamentsTestLeadersOfSellsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
   # sys.exit(not result.wasSuccessful())
