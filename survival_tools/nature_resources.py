class NatureResources:
    def __init__(self):
        self.resources = {
            "Tree Sap": (
                "Tree sap serves as a natural adhesive and fire starter:\n"
                "- **Adhesive**: Use sap to bind materials for constructing shelters or creating tools.\n"
                "- **Fire Starter**: Sap from pine trees is highly flammable and can be used to start a fire even in damp conditions."
            ),
            "Plant Fibers": (
                "Plant fibers can be used to create cordage, essential for survival tasks such as shelter building, trapping, and tool-making:\n"
                "- **Cordage**: Harvest fibers from plants like nettles, flax, or tree bark to make ropes or strings."
            ),
            "Stone Tools": (
                "Stones can be shaped into various tools using knapping techniques. These tools can be used for cutting, scraping, or as weapons:\n"
                "- **Sharp Blades**: Create sharp edges by striking flint or obsidian against a harder stone."
            ),
            "Natural Insulation": (
                "Use nature to insulate your shelter and protect yourself from the cold:\n"
                "- **Leaves, Grass, Moss**: Layer dry plant materials between you and the ground for insulation."
            ),
            "Water from Plants": (
                "Certain plants provide water, which can be life-saving in arid environments:\n"
                "- **Cacti**: In desert regions, extract water from cactus plants. Use only non-toxic varieties like the prickly pear."
            ),
            "Animal Resources": (
                "In survival scenarios, animals provide food, materials for clothing, and tools:\n"
                "- **Leather and Fur**: Use animal hides to make clothing or bedding in cold climates.\n"
                "- **Bones**: Animal bones can be fashioned into tools, weapons, or needles for sewing."
            ),
        }

    def get_nature_resources(self):
        """Returns nature-based survival resources."""
        return self.resources

    def recommend_resource(self, need):
        """
        Recommends natural resources based on survival needs.
        Needs: 'fire', 'tools', 'water', 'insulation', 'adhesive', 'clothing'.
        """
        if need == "fire":
            return "Use tree sap as a natural fire starter. Combine it with dry plant fibers for tinder."
        elif need == "tools":
            return "Create stone tools by knapping sharp stones for cutting and scraping tasks."
        elif need == "water":
            return "Extract water from non-toxic plants like cacti in the desert. Use vines in tropical regions for water."
        elif need == "insulation":
            return "Use leaves, grass, or moss to insulate your shelter and bedding."
        elif need == "adhesive":
            return "Tree sap is a natural adhesive that can be used to bind materials or waterproof containers."
        elif need == "clothing":
            return "Use animal hides for clothing or bedding to protect yourself from the cold."
        else:
            return "Utilize plant fibers for essential tasks like creating cordage, which can be used for trapping, shelter-building, and tool-making."

# Example usage
if __name__ == "__main__":
    nature_resources = NatureResources()
    print(nature_resources.get_nature_resources())
    print(nature_resources.recommend_resource('fire'))
