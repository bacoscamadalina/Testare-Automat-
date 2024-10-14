import unittest
import HtmlTestRunner
from Alerte import Alert
from Formy import TestLogin


class TestSuite(unittest.TestCase):
    def test_suite(self):
        # Creează o instanță a suitei de teste
        suite = unittest.TestSuite()

        # Adaugă testele din clasa Alert la suită
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Alert))
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))

        # Creează un obiect HtmlTestRunner
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Smoke Testing Report",
            report_name="Raport_complet"
        )

        # Rulează testele și generează raportul HTML
        runner.run(suite)