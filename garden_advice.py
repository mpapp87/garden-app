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
    season = season.strip().lower()
    plant_type = plant_type.strip().lower()
    seasonal_tip = SEASON_ADVICE.get(season, "No advice for this season.")
    plant_tip = PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")
    return f"{seasonal_tip}\n{plant_tip}"


def read_choice(label, choices):
    """Prompt until a supported choice is entered, ignoring case and spaces."""
    options = ", ".join(choices)
    while True:
        choice = input(f"Enter {label} ({options}): ").strip().lower()
        if choice in choices:
            return choice
        print(f"Please choose one of: {options}.")


def main():
    """Read gardening preferences and display advice; cancel gracefully."""
    try:
        season = read_choice("season", SEASON_ADVICE)
        plant_type = read_choice("plant type", PLANT_ADVICE)
    except (EOFError, KeyboardInterrupt):
        print("\nGardening advice cancelled.")
        return
    print(get_gardening_advice(season, plant_type))


if __name__ == "__main__":
    main()
