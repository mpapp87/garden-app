# garden-app

Gardening advice for the HyperionDev M07T02 Git Workflows task, based on the supplied `garden_advice.py` starter.

Run with Python 3:

```sh
python3 garden_advice.py
```

Run the regression tests:

```sh
python3 -m unittest -v
```

Advice generation is separated from the command-line entry point. Seasonal and plant tips are stored in dictionaries, and unknown choices retain the original fallback messages.

Choose `summer` or `winter`, then `flower` or `vegetable`. Capitalization and surrounding spaces are ignored. Blank or unsupported entries are explained and re-prompted. Ctrl-C or end-of-input cancels cleanly.

Example:

```text
Enter season (summer, winter): WINTER
Enter plant type (flower, vegetable): flower
Protect your plants from frost with covers.
Use fertiliser to encourage blooms.
```

The app retains the starter's supported seasons and plants. It uses the season entered by the gardener rather than inferring it from a month, so it does not assume a hemisphere. Advice is general and may need adapting to local conditions.

## Git workflow

- Issue #1: refactor the starter into documented functions and dictionaries, with regression tests; branch `issue-1-refactor-advice`.
- Issue #2: replace hardcoded choices with validated interactive input; branch `issue-2-user-input`.
- Each change is developed and committed locally, pushed to GitHub, and submitted through a separate pull request into `main`.
