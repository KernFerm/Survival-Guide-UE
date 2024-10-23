class FoodTools:
    def __init__(self):
        self.food_sources = {
            "Berries": (
                "Edible varieties include blackberries, raspberries, and blueberries. Always ensure proper identification to avoid poisoning."
            ),
            "Edible Plants": (
                "Common edible plants include dandelions, cattails, and wild onions. Ensure you are familiar with local plant species to avoid toxic varieties."
            ),
            "Trapping": (
                "Set snares and deadfall traps to catch small game like rabbits and squirrels. Learn basic trap-making techniques to increase your success."
            ),
            "Fishing": (
                "Freshwater fishing is one of the most reliable survival food sources. Create fishing lines, hooks, and nets from available materials."
            ),
            "Foraging": (
                "Forage nuts, seeds, mushrooms, and roots. Avoid mushrooms unless you are certain of their edibility. Some varieties are highly toxic."
            ),
            "Food Preservation": (
                "Dry meat and fish using sun or smoke. Salting is another method of preservation if salt is available. Preserve fruits by drying them in the sun."
            ),
        }

    def get_all_food_sources(self):
        """Returns available food sources from nature."""
        return self.food_sources

    def recommend_food(self, region, season="summer"):
        """
        Recommends food sources based on region and season.
        Regions: 'forest', 'desert', 'mountain', 'riverbank', 'plains', 'tundra'.
        Seasons: 'summer', 'winter', 'spring', 'fall'.
        """
        if region == "forest":
            if season in ['summer', 'fall']:
                return "Forage for berries, edible plants, and set traps for small game. In fall, nuts and seeds are plentiful."
            elif season == "winter":
                return "Focus on trapping and fishing, as plants and berries will be scarce."
        elif region == "desert":
            return "Focus on trapping small game like lizards and foraging water-rich plants like cacti."
        elif region == "mountain":
            return "Hunt small game and fish in mountain streams. Edible plants are more common in lower valleys."
        elif region == "riverbank":
            return "Fishing is your best bet near rivers. Forage for edible plants along the water's edge."
        elif region == "plains":
            return "Set traps for small animals like rabbits and forage for roots, seeds, and grasses."
        elif region == "tundra":
            return "In cold regions, focus on trapping and fishing. Plants are rare, but edible roots may be found."
        else:
            return "Focus on trapping and fishing in most survival scenarios."

# Example usage
if __name__ == "__main__":
    food_tools = FoodTools()
    print(food_tools.get_all_food_sources())
    print(food_tools.recommend_food('forest', 'summer'))
