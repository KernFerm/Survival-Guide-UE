class ShelterTools:
    def __init__(self):
        self.materials = {
            "Branches": (
                "Use for building frameworks for lean-tos, A-frame shelters, and debris huts. The branches must be sturdy enough to "
                "support additional weight such as leaves or snow."
            ),
            "Leaves": (
                "Leaves can provide excellent insulation when layered thickly. Use as roof cover, bedding, and windbreaks. "
                "Dry leaves are best for keeping out the cold."
            ),
            "Rocks": (
                "Rocks are great for creating barriers and windbreaks. In cold weather, heated rocks can also be placed inside the shelter "
                "to provide warmth."
            ),
            "Mud": (
                "Mud can seal cracks in shelters, providing insulation and making the shelter more waterproof. It’s particularly useful in "
                "areas with heavy rain or cold weather."
            ),
            "Snow": (
                "In extreme cold, snow can be used to build igloos or snow caves, which trap heat. When done correctly, these shelters can "
                "be surprisingly warm."
            ),
            "Tarp": (
                "A tarp or plastic sheet can be invaluable for quick shelter construction. Use it to create an instant waterproof roof, "
                "ground cover, or windbreak. In the desert, it can be used to create a shade shelter."
            ),
        }

    def get_all_materials(self):
        """Returns available materials for building shelters."""
        return self.materials

    def suggest_shelter(self, environment, weather="clear"):
        """
        Suggests the best shelter-building techniques based on environment and weather.
        Environments: 'forest', 'desert', 'mountain', 'snow', 'plains', 'swamp'.
        Weather: 'rainy', 'clear', 'windy', 'snowy', 'cold', 'hot'.
        """
        if environment == "forest":
            if weather in ['rainy', 'cold']:
                return "Build a debris hut using branches and leaves for insulation and rain protection."
            else:
                return "A simple lean-to shelter using branches and leaves will work well in moderate weather."
        elif environment == "desert":
            return "Use rocks and a tarp to create shade. In sandy areas, dig down to cooler ground for relief from the heat."
        elif environment == "mountain":
            return "Use rocks and branches to build a shelter that protects from wind. Insulate with leaves or snow if available."
        elif environment == "snow":
            return "Build a snow cave or igloo for insulation. Snow traps heat effectively if built correctly."
        elif environment == "plains":
            return "In open areas, use a tarp to create an A-frame shelter. Anchor it with rocks or stakes."
        elif environment == "swamp":
            return "Build your shelter off the ground using branches and rocks to avoid dampness and insects."
        else:
            return "A-frame or lean-to shelters are versatile and can be built in most environments with the right materials."

# Example usage
if __name__ == "__main__":
    shelter_tools = ShelterTools()
    print(shelter_tools.get_all_materials())
    print(shelter_tools.suggest_shelter('forest', 'rainy'))
