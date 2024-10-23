class WaterTools:
    def __init__(self):
        self.water_sources = {
            "Streams": (
                "Streams and rivers provide a reliable source of water. Always purify water from natural sources to avoid pathogens."
            ),
            "Rainwater": (
                "Collect rainwater using tarps, plastic sheets, or large leaves. In survival situations, rainwater is usually safe to drink, but boiling is recommended if uncertain."
            ),
            "Dew Collection": (
                "Collect dew from grass and plants using a cloth or plastic bag. In dry areas, dew collection can provide small amounts of water."
            ),
            "Solar Still": (
                "A solar still uses the sun to evaporate water from the ground. Dig a hole, place a container in the center, and cover it with plastic to condense water."
            ),
            "Cacti": (
                "In desert regions, some cacti can provide water. Be careful when harvesting cactus water, as not all species are safe to consume."
            ),
            "Transpiration Bags": (
                "Place a plastic bag over a leafy tree branch to collect water through transpiration. This method can produce small amounts of clean water over several hours."
            ),
        }

    def get_all_water_sources(self):
        """Returns available water sources in nature."""
        return self.water_sources

    def recommend_water_source(self, region):
        """
        Recommends water sources based on region.
        Regions: 'forest', 'desert', 'mountain', 'riverbank', 'plains', 'tundra'.
        """
        if region == "forest":
            return "Look for streams and rivers. Rainwater collection and dew collection are also viable."
        elif region == "desert":
            return "Focus on solar stills, dew collection, and harvesting water from cacti."
        elif region == "mountain":
            return "Mountain streams and snowmelt are common water sources, but always purify before drinking."
        elif region == "riverbank":
            return "Rivers provide a constant water source, but boiling or filtering is necessary."
        elif region == "plains":
            return "Look for natural rainwater collection points and use dew collection methods."
        elif region == "tundra":
            return "Melt snow or ice, but always boil or filter to avoid contaminants."
        else:
            return "Dew collection and rainwater are usually the safest and easiest methods in most environments."

    def purify_water(self, method="boiling"):
        """
        Purifies water using various methods.
        Methods: 'boiling', 'solar', 'chemical', 'filtration'.
        """
        if method == "boiling":
            return "Boil water for at least 5-10 minutes to kill bacteria, parasites, and viruses."
        elif method == "solar":
            return "Use a clear plastic bottle and expose the water to sunlight for several hours to kill pathogens through UV radiation."
        elif method == "chemical":
            return "Use iodine or chlorine tablets to disinfect water. Follow dosage instructions carefully."
        elif method == "filtration":
            return "Use a portable filter or create a DIY filter with sand, charcoal, and gravel to remove large particles and impurities."
        else:
            return "Boiling is the most reliable and effective method for water purification."

# Example usage
if __name__ == "__main__":
    water_tools = WaterTools()
    print(water_tools.get_all_water_sources())
    print(water_tools.recommend_water_source('desert'))
    print(water_tools.purify_water('boiling'))
