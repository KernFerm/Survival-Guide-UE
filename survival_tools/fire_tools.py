class FireTools:
    def __init__(self):
        self.techniques = {
            "Flint and Steel": (
                "Sparks from the flint are used to ignite dry tinder. Ensure the tinder is dry and finely shredded for best results."
            ),
            "Bow Drill": (
                "Friction fire technique using a spindle and bow. Works best with softwood. Requires patience and practice. "
                "Ensure both wood pieces are dry and find a dry leaf to catch the ember."
            ),
            "Fire Plough": (
                "Another friction-based fire starter. Rub a hard stick (plough) against a softer piece of wood (base) "
                "to create friction and generate an ember."
            ),
            "Solar Ignition": (
                "Using a magnifying glass or any clear convex lens, focus sunlight onto tinder. Best used on clear, sunny days. "
                "Ensure tinder is dry and easily combustible, such as dry grass or bark."
            ),
            "Hand Drill": (
                "Similar to the bow drill, but uses hands to spin the spindle instead of a bow. More challenging due to the "
                "energy and dexterity required. Works well in dry environments with softwood."
            ),
            "Natural Tinder": (
                "Use dry grass, bark, leaves, or resinous wood as tinder. Create a tinder nest by finely shredding materials. "
                "Gather as much as possible before attempting to start a fire."
            ),
            "Char Cloth": (
                "Create char cloth by burning cotton or linen in a sealed metal container with a small hole. This blackened cloth "
                "easily catches sparks and ignites quickly."
            ),
            "Using Fungus": (
                "Certain types of fungus (e.g., tinder fungus) can catch a spark and burn slowly. These are found in forests "
                "on decaying trees and are great in wet conditions."
            ),
        }

    def get_all_techniques(self):
        """Returns all available fire-starting techniques."""
        return self.techniques

    def recommend_technique(self, condition="general"):
        """
        Recommends the best fire-starting technique based on conditions like weather, terrain, or available materials.
        Example conditions: 'rainy', 'dry', 'windy', 'woodland', 'sunny', 'cold'.
        """
        if condition == "rainy":
            return "Flint and Steel or Char Cloth are reliable even in wet conditions. Keep tinder dry!"
        elif condition == "dry":
            return "Fire Plough works best in dry conditions. Bow Drill is also effective if wood is available."
        elif condition == "woodland":
            return "The Bow Drill or Hand Drill can be effective in forest environments with the right dry wood."
        elif condition == "sunny":
            return "Solar Ignition is ideal on bright sunny days. No need for matches or lighters."
        elif condition == "cold":
            return "Flint and Steel with char cloth will work in cold environments if your hands are too cold to use other methods."
        else:
            return "Flint and Steel is a reliable all-weather technique that works in most environments."

# Example usage
if __name__ == "__main__":
    fire_tools = FireTools()
    print(fire_tools.get_all_techniques())
    print(fire_tools.recommend_technique('rainy'))
