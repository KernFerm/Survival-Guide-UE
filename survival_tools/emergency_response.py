class EmergencyResponse:
    def __init__(self):
        self.strategies = {
            "Earthquake": (
                "During an earthquake:\n"
                "- **Indoors**: Drop to the ground, take cover under sturdy furniture, and hold on until the shaking stops. "
                "Stay away from windows, mirrors, and heavy objects that could fall.\n"
                "- **Outdoors**: Move to an open area away from buildings, trees, and utility wires."
            ),
            "Flood": (
                "During a flood:\n"
                "- Move to higher ground immediately. Never walk or drive through floodwaters.\n"
                "- Use a flotation device or secure yourself with a rope if crossing a flooded area is necessary."
            ),
            "Wildfire": (
                "If you are near a wildfire:\n"
                "- Evacuate the area as soon as possible. If trapped, create a firebreak by clearing vegetation.\n"
                "- Take shelter in a low-lying area and cover yourself with wet clothing or soil to protect against heat and flames."
            ),
            "Grid-Down Scenario": (
                "In grid-down situations (power and communication loss):\n"
                "- Prepare a bug-out bag with essential items like food, water, first aid, and communication devices (walkie-talkies).\n"
                "- Establish a communication plan with family or group members in case cell towers and power go down."
            ),
            "Pandemic": (
                "During a pandemic:\n"
                "- Isolate yourself and limit contact with others to prevent the spread of the disease.\n"
                "- Stock up on medical supplies, masks, and disinfectants. Stay informed through reliable news sources."
            ),
            "Hurricane": (
                "In the event of a hurricane:\n"
                "- Secure windows and doors with plywood. Move to a safe area inside your home (e.g., a basement or interior room).\n"
                "- Have emergency supplies ready, including water, food, and first aid. Prepare to evacuate if directed by local authorities."
            ),
            "Tsunami": (
                "If you are near the coast during a tsunami warning:\n"
                "- Move to higher ground immediately. Do not wait for official evacuation orders.\n"
                "- Stay away from the shore even after the first wave hits, as tsunamis come in multiple waves that can continue for hours."
            ),
        }

    def get_emergency_strategies(self):
        """Returns strategies for different world events and disasters."""
        return self.strategies

    def recommend_strategy(self, event):
        """
        Recommends strategies based on specific world events and natural disasters.
        Events: 'earthquake', 'flood', 'wildfire', 'grid-down', 'pandemic', 'hurricane', 'tsunami'.
        """
        if event == "earthquake":
            return "Drop, cover, and hold on during the quake. Move to an open area if you are outdoors."
        elif event == "flood":
            return "Move to higher ground immediately and avoid walking or driving through floodwaters."
        elif event == "wildfire":
            return "Evacuate early. If trapped, create a firebreak and seek shelter in low-lying areas."
        elif event == "grid-down":
            return "Prepare a bug-out bag with essential supplies and establish a communication plan with loved ones."
        elif event == "pandemic":
            return "Isolate to prevent disease spread, stock up on medical supplies, and stay informed."
        elif event == "hurricane":
            return "Secure windows and doors. Move to a safe area in your home and prepare emergency supplies."
        elif event == "tsunami":
            return "Move to higher ground immediately. Avoid the shoreline, as multiple tsunami waves can follow."
        else:
            return "Focus on general disaster preparedness, including securing food, water, and shelter."

# Example usage
if __name__ == "__main__":
    emergency_response = EmergencyResponse()
    print(emergency_response.get_emergency_strategies())
    print(emergency_response.recommend_strategy('hurricane'))
