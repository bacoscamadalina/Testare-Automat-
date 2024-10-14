import unittest
import HtmlTestRunner
from Tema1 import TestForm1
from Tema2 import TestForm2
from Tema3 import TestForm3
from Tema4 import TestForm4


class TestSuite(unittest.TestCase):
    def test_suite(self):
        suite= unittest.TestSuite()

        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestForm1))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestForm2))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestForm3))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestForm4))

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Teste Teme 1,2,3,4',
            report_name = 'Raport_complet'
        )

        runner.run(suite)