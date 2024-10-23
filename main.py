from survival_tools.fire_tools import FireTools
from survival_tools.shelter_tools import ShelterTools
from survival_tools.food_tools import FoodTools
from survival_tools.water_tools import WaterTools
from survival_tools.water_tracker import WaterTracker

def main():
    print("Welcome to the Survival Guide!")

    # Fire Starting Techniques
    fire_tools = FireTools()
    print("\nFire Starting Techniques:")
    for technique, description in fire_tools.get_all_techniques().items():
        print(f"- {technique}: {description}")

    # Shelter Building Materials
    shelter_tools = ShelterTools()
    print("\nShelter Building Materials:")
    for material, usage in shelter_tools.get_all_materials().items():
        print(f"- {material}: {usage}")

    # Food Foraging
    food_tools = FoodTools()
    print("\nForaging Food Sources:")
    for food, info in food_tools.get_all_food_sources().items():
        print(f"- {food}: {info}")

    # Water Procurement and Purification
    water_tools = WaterTools()
    print("\nWater Sources and Purification Methods:")
    print(f"Water source: {water_tools.recommend_water_source('forest')}")
    print(f"Purification method: {water_tools.purify_water('boiling')}")

    # Water Consumption Tracking
    tracker = WaterTracker(10)  # Assume 10 liters of water
    tracker.consume_water(2)
    print(f"\nWater left: {tracker.water_left()} liters")
    tracker.generate_chart()

if __name__ == "__main__":
    main()
