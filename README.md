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
