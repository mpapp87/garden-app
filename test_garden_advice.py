"""Regression tests for the original gardening advice behavior."""

import io
from contextlib import redirect_stdout
from unittest.mock import patch

import subprocess
import sys
import unittest
from pathlib import Path

from garden_advice import get_gardening_advice, main, read_choice


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


class InputTests(unittest.TestCase):
    def test_normalizes_advice_arguments(self):
        self.assertEqual(get_gardening_advice(" SUMMER ", " Flower "),
                         get_gardening_advice("summer", "flower"))

    def test_reprompts_for_blank_and_unsupported_choices(self):
        with patch("builtins.input", side_effect=["", "monsoon", " Winter "]) as prompt:
            with redirect_stdout(io.StringIO()) as output:
                self.assertEqual(read_choice("season", ("summer", "winter")), "winter")
        self.assertEqual(prompt.call_count, 3)
        self.assertEqual(output.getvalue().count("Please choose one of:"), 2)

    def test_interactive_script(self):
        result = subprocess.run([sys.executable, "garden_advice.py"],
                                input="SUMMER\n\nTREE\n vegetable \n",
                                cwd=Path(__file__).parent, text=True,
                                capture_output=True, check=True)
        self.assertIn("Water your plants regularly and provide some shade.", result.stdout)
        self.assertIn("Keep an eye out for pests!", result.stdout)
        self.assertEqual(result.stdout.count("Please choose one of:"), 2)
        self.assertEqual(result.stderr, "")

    def test_cancellation_at_either_prompt(self):
        for error in (EOFError, KeyboardInterrupt):
            for answers in ([error], ["summer", error]):
                with self.subTest(error=error, answers=answers):
                    with patch("builtins.input", side_effect=answers):
                        with redirect_stdout(io.StringIO()) as output:
                            main()
                    self.assertIn("Gardening advice cancelled.", output.getvalue())
                    self.assertNotIn("Water your plants", output.getvalue())


if __name__ == "__main__":
    unittest.main()
