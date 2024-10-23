# Survival Guide in Python 🏞️🛠️

## Overview

This comprehensive **Survival Guide** equips you with the tools, techniques, and strategies to survive in various challenging scenarios, including wilderness survival, apocalyptic events, world disasters, and grid-down situations. It includes modules for fire-starting, shelter-building, food foraging, water procurement, navigation, and emergency response. The guide is designed to be flexible, allowing users to modify it for their specific survival needs.

---

### Project Structure

```
survival_guide/
│
├── survival_tools/
│   ├── __init__.py (package initialization)
│   ├── fire_tools.py (fire-starting techniques for all environments)
│   ├── shelter_tools.py (shelter-building techniques across various climates)
│   ├── food_tools.py (foraging, hunting, and food preservation methods)
│   ├── water_tools.py (locating, purifying, and rationing water)
│   ├── navigation_tools.py (compass, sun, star navigation, and signaling)
│   ├── apocalypse_tools.py (apocalyptic survival tools, defense, and bartering)
│   ├── nature_resources.py (using nature as a resource in survival situations)
│   ├── emergency_response.py (emergency response for disasters and grid-down scenarios)
│   ├── water_tracker.py (water and food consumption tracker with rationing)
│
├── main.py (main entry point to access all survival tools)
├── README.md (this guide)
└── requirements.txt (lists Python dependencies)
```


---

## Features

- **Fire Starting Techniques** 🔥  
  Learn to start a fire using tools and nature-based methods:
  - Flint and Steel
  - Bow Drill
  - Fire Plough
  - Solar Ignition
  - Natural Tinder (dry leaves, grass, bark)
  - Char Cloth and Fungus for fire-starting

- **Shelter Building** 🏕️  
  Find out how to build shelters using:
  - Branches for framework
  - Leaves for insulation
  - Rocks for protection
  - Mud for sealing gaps
  - Snow for igloos and snow caves
  - Tarp for quick shelter setup

- **Foraging and Hunting** 🍃🐟  
  Gather food through foraging, trapping, and fishing:
  - Berries, edible plants, mushrooms (with caution)
  - Small animal traps (e.g., snares, deadfall traps)
  - Fishing in rivers, lakes, and streams
  - Long-term food storage (drying, smoking, salting)

- **Water Procurement and Purification** 💧  
  Learn to find and purify water using:
  - Streams, rivers, and rainwater collection
  - Solar stills, dew collection, and transpiration bags
  - Boiling, solar disinfection, chemical purification, filtration

- **Navigation Tools** 🧭  
  Navigate using:
  - Compass
  - Sun and Shadows for direction
  - Star Navigation (North Star, constellations)
  - Moss on trees for natural navigation
  - Signaling methods for rescue (smoke signals, reflective surfaces)

- **Apocalyptic Survival Tools** 🛡️  
  Survive in long-term apocalyptic scenarios with:
  - Makeshift weapons (spears, slingshots, Molotov cocktails)
  - Fortifying shelters using natural barriers and traps
  - Bartering for essential goods (food, water, medicine)
  - Creating defensive perimeters with noise-making alarms

- **Using Nature as a Resource** 🌿  
  Discover how nature can help you survive:
  - Tree sap as adhesive and fire starter
  - Plant fibers for cordage (ropes, snares, shelter construction)
  - Stone tools for cutting and scraping
  - Natural insulation (leaves, grass, moss)
  - Water extraction from plants (cacti, vines)

- **Emergency Response Strategies** 🚨  
  Prepare for world events and natural disasters:
  - Earthquakes, floods, wildfires, hurricanes, and tsunamis
  - Grid-down scenarios (prepare bug-out bags, communication plans)
  - Pandemic isolation and quarantine techniques

- **Water and Food Rationing** 🥤🍲  
  Manage your resources using the advanced water and food tracker:
  - Track daily consumption of water and food
  - Calculate rations based on remaining resources and days left
  - Visualize consumption with charts for water and food
  - Ration recommendations for specific environments (arctic, desert, rainforest)

---

### [Python 3.11.6](https://github.com/KernFerm/Py3.11.6installer)

---

## Installation

1. Clone the repository or download the project files:
```
git clone https://github.com/kernferm/survival_guide.git
```

2. **Create a virtual environment (optional but recommended):**

```
python -m venv venv
```

3. **Activate the virtual environment:**

- ***On Windows:***

```
venv\Scripts\activate
```

- ***On macOS/Linux***

```
source venv/bin/activate
```

4. **Install the required dependencies:**

```
pip install -r requirements.txt
```

## How to Use the Project

1. **Run the Project
- Run the main script to start using the survival tools:

```
python main.py
```

2. **Choose a Module**

Follow the on-screen prompts to select which survival tool you want to explore, whether it's fire-starting, shelter-building, food gathering, or water procurement.

3. **Water and Food Tracking**

Use the water tracker to manage your water and food supplies. You can track your consumption and receive daily ration recommendations based on the days you need to survive:

```
python water_tracker.py
```

4. **Customize the Guide**

You can modify any of the modules to better suit your personal needs or the environment you expect to encounter:

- **Change fire-starting techniques** in `fire_tools.py` to reflect the resources available in your region.

- **New survival strategies** for `arctic`, `desert`, or `rainforest` conditions.

- **New emergency response plans** for specific disasters.

## Water and Food Consumption Tracker

The water and food tracker helps you manage your consumption and rationing during survival situations. After consuming water or food, a pie chart will display the remaining resources. You can also receive daily ration recommendations based on your needs.

### Example Usage:

- Start by setting how much water and food you have available:

```
python water_tracker.py
```

- Visualize water and food consumption with charts to plan your resources better.

## Customizing for Your Needs

You can easily edit the survival guide to best suit your needs. Here’s how:

- **Change Region-Specific Techniques:**
If you're planning for a specific location (e.g., desert survival), edit the files in `survival_tools/` to reflect that environment.

- **Add Your Own Emergency Responses:**
Modify `emergency_response.py` to include disaster preparedness strategies for events more common in your area, such as hurricanes or tornadoes.

- **Modify Water and Food Rationing:**
Update `water_tracker.py` to customize how much water or food is needed for your daily rations, based on personal or family needs.

## License

***This project is open-source and available for anyone to use. Contributions are welcome! Feel free to fork the repository, improve the project, or submit a pull request.***

## Credits

Developed by `Bubbles The Dev`, dedicated to providing accessible survival knowledge for everyone. 🌍🌱
