class ApocalypseTools:
    def __init__(self):
        self.apocalypse_tools = {
            "Makeshift Weapons": (
                "In apocalyptic events, you'll need weapons for self-defense and hunting. Common makeshift weapons include:\n"
                "- **Spears**: Use long sticks or metal rods with sharpened ends.\n"
                "- **Slingshots**: Made using rubber tubing and scrap material for hunting small game.\n"
                "- **Clubs**: Heavy sticks or pipes can serve as blunt weapons. Attach nails or sharp objects to increase lethality.\n"
                "- **Molotov Cocktails**: Use bottles filled with flammable liquids as throwable incendiaries."
            ),
            "Fortifying Shelter": (
                "Fortifying your shelter is essential to protect against intruders and wildlife. Methods include:\n"
                "- **Barricades**: Use debris, logs, or rocks to block entry points.\n"
                "- **Traps**: Set up tripwires with noise-makers or create pitfall traps around your shelter.\n"
                "- **Hidden Entrances**: Camouflage shelter doors and windows to reduce visibility."
            ),
            "Bartering": (
                "In a collapsed economy, bartering will replace currency. Items that become valuable include:\n"
                "- **Food and Water**: High-demand items for bartering.\n"
                "- **Medicine**: Antibiotics, pain relievers, and medical supplies will be crucial.\n"
                "- **Fuel and Tools**: Items like gas, batteries, and knives are worth a lot.\n"
                "- **Weapons and Ammunition**: Highly valuable for defense and hunting."
            ),
            "Defense Perimeter": (
                "Defending your shelter requires early warning systems and protective measures:\n"
                "- **Noise-Making Alarms**: Set up cans or scrap metal along perimeters that will make noise if disturbed.\n"
                "- **Booby Traps**: Create simple traps such as spikes or pits around your perimeter."
            ),
            "Sustainable Food and Water": (
                "In apocalyptic scenarios, finding sustainable sources of food and water is critical for long-term survival:\n"
                "- **Gardening**: Start a garden with fast-growing crops like potatoes, beans, and leafy greens.\n"
                "- **Rainwater Collection**: Use tarps or containers to collect rainwater, which can be filtered for drinking.\n"
                "- **Hunting and Fishing**: Small game traps, fishing nets, and basic hunting tools are vital for acquiring protein."
            ),
        }

    def get_apocalypse_tools(self):
        """Returns all apocalypse survival tools and techniques."""
        return self.apocalypse_tools

    def recommend_tool(self, scenario):
        """
        Recommends tools or techniques based on apocalyptic scenarios.
        Scenarios: 'defense', 'bartering', 'shelter', 'long-term survival'.
        """
        if scenario == "defense":
            return (
                "For defense, create makeshift weapons such as spears, slingshots, and clubs. Set up noise-making alarms around your "
                "shelter to detect intruders, and fortify your shelter using barricades and camouflage."
            )
        elif scenario == "bartering":
            return (
                "To prepare for bartering, stockpile essential goods such as food, water, medicine, and fuel. "
                "Keep your trading items secure and only barter with trustworthy individuals."
            )
        elif scenario == "shelter":
            return (
                "To fortify your shelter, create barricades with available debris and rocks. Consider setting up traps or "
                "camouflaging entry points to reduce visibility."
            )
        elif scenario == "long-term survival":
            return (
                "For long-term survival, establish a garden for growing food, set up rainwater collection systems, and use "
                "hunting and fishing techniques to supplement your diet."
            )
        else:
            return "General survival tip: Ensure multiple exit points from your shelter in case of attack."

# Example usage
if __name__ == "__main__":
    apocalypse_tools = ApocalypseTools()
    print(apocalypse_tools.get_apocalypse_tools())
    print(apocalypse_tools.recommend_tool('defense'))
