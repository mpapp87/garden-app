"""Generate simple gardening advice from a season and plant type."""

SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}
PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}


def get_gardening_advice(season, plant_type):
    """Combine seasonal and plant advice, with fallbacks for unknown choices."""
    seasonal_tip = SEASON_ADVICE.get(season, "No advice for this season.")
    plant_tip = PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")
    return f"{seasonal_tip}\n{plant_tip}"


def main():
    """Display the starter example when this file is run directly."""
    # TODO: Replace these defaults with validated user input.
    print(get_gardening_advice("summer", "flower"))


if __name__ == "__main__":
    main()
