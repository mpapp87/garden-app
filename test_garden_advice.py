"""Regression tests for the original gardening advice behavior."""

import subprocess
import sys
import unittest
from pathlib import Path

from garden_advice import get_gardening_advice


class AdviceTests(unittest.TestCase):
    def test_supported_combinations(self):
        seasons = {
            "summer": "Water your plants regularly and provide some shade.",
            "winter": "Protect your plants from frost with covers.",
        }
        plants = {
            "flower": "Use fertiliser to encourage blooms.",
            "vegetable": "Keep an eye out for pests!",
        }
        for season, seasonal_tip in seasons.items():
            for plant, plant_tip in plants.items():
                with self.subTest(season=season, plant=plant):
                    self.assertEqual(get_gardening_advice(season, plant),
                                     f"{seasonal_tip}\n{plant_tip}")

    def test_unknown_season_preserves_plant_advice(self):
        self.assertEqual(get_gardening_advice("spring", "flower"),
                         "No advice for this season.\nUse fertiliser to encourage blooms.")

    def test_unknown_plant_preserves_season_advice(self):
        self.assertEqual(get_gardening_advice("winter", "tree"),
                         "Protect your plants from frost with covers.\nNo advice for this type of plant.")

    def test_unknown_choices(self):
        self.assertEqual(get_gardening_advice("", ""),
                         "No advice for this season.\nNo advice for this type of plant.")

    def test_import_has_no_output(self):
        result = subprocess.run([sys.executable, "-c", "import garden_advice"],
                                cwd=Path(__file__).parent, capture_output=True,
                                text=True, check=True)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
