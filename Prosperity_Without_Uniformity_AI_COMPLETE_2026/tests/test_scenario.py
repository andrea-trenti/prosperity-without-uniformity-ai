"""Unit tests for illustrative algebra; these do not validate the economic forecast."""
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'models'))
from scenario import Product


class ScenarioTests(unittest.TestCase):
    def setUp(self):
        self.m = Product()

    def test_input_unit_cost(self):
        self.assertEqual(self.m.unit_cost_0, 600)
        self.assertAlmostEqual(self.m.unit_cost_1, 310)

    def test_temporary_margin_increase_if_price_static(self):
        r = self.m.scenario(1000, 0.5)
        self.assertAlmostEqual(r['margin_0_EUR'], 400)
        self.assertAlmostEqual(r['margin_1_EUR'], 690)

    def test_100_euro_case_not_profitable_under_default_costs(self):
        r = self.m.scenario(100, 1.2)
        self.assertTrue(r['price_below_cost'])
        self.assertAlmostEqual(r['margin_1_EUR'], -210)

    def test_revenue_changes_with_elasticity(self):
        low = self.m.scenario(100, 0.5)
        high = self.m.scenario(100, 1.2)
        self.assertAlmostEqual(low['revenue_ratio'], math.sqrt(.1), places=8)
        self.assertGreater(high['revenue_ratio'], 1)

    def test_no_employment_guarantee(self):
        high = self.m.scenario(100, 1.2)
        low = self.m.scenario(100, 0.5)
        self.assertGreater(high['labor_hours_ratio_total'], 1)
        self.assertLess(low['labor_hours_ratio_total'], 1)

    def test_invalid_automation(self):
        with self.assertRaises(ValueError):
            Product(automation_fraction=1.2)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            self.m.scenario(0, 1)


if __name__ == '__main__':
    unittest.main()
