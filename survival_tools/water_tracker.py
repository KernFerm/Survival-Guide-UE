import matplotlib.pyplot as plt

class WaterTracker:
    def __init__(self, total_water, total_food):
        if total_water <= 0:
            raise ValueError("Total water must be greater than zero.")
        if total_food <= 0:
            raise ValueError("Total food must be greater than zero.")
        
        self.total_water = total_water  # Total water in liters
        self.consumed_water = 0         # Water consumed in liters
        self.total_food = total_food    # Total food in kilograms
        self.consumed_food = 0          # Food consumed in kilograms

    def consume_water(self, liters):
        """Tracks water consumption."""
        if liters <= 0:
            raise ValueError("Consumed water must be a positive number.")
        if liters > (self.total_water - self.consumed_water):
            raise ValueError("Not enough water left to consume that amount.")
        self.consumed_water += liters

    def consume_food(self, kilograms):
        """Tracks food consumption."""
        if kilograms <= 0:
            raise ValueError("Consumed food must be a positive number.")
        if kilograms > (self.total_food - self.consumed_food):
            raise ValueError("Not enough food left to consume that amount.")
        self.consumed_food += kilograms

    def water_left(self):
        """Returns the amount of water left."""
        return self.total_water - self.consumed_water

    def food_left(self):
        """Returns the amount of food left."""
        return self.total_food - self.consumed_food

    def recommend_ration(self, days_left, resource="water", environment="default"):
        """
        Recommends daily rations based on remaining resources and environment.
        Resource: 'water' or 'food'.
        Environments: 'arctic', 'desert', 'rainforest', 'default'.
        """
        if days_left <= 0:
            raise ValueError("Days left must be greater than zero.")
        
        if environment == "desert":
            water_ration_multiplier = 1.5  # Need more water in hot climates
        elif environment == "arctic":
            water_ration_multiplier = 0.8  # Need slightly less water in cold climates
        elif environment == "rainforest":
            water_ration_multiplier = 1.0  # Normal water consumption, with focus on avoiding contamination
        else:
            water_ration_multiplier = 1.0  # Default water rationing

        if resource == "water":
            return (self.water_left() / days_left) * water_ration_multiplier
        elif resource == "food":
            return self.food_left() / days_left
        else:
            return "Invalid resource. Choose 'water' or 'food'."

    def generate_chart(self):
        """Generates pie charts showing water and food consumption."""
        water_left = self.water_left()
        food_left = self.food_left()

        # Water chart
        plt.subplot(1, 2, 1)
        data_water = [self.consumed_water, water_left]
        labels_water = ['Consumed Water', 'Water Left']
        plt.pie(data_water, labels=labels_water, autopct='%1.1f%%', startangle=90)
        plt.title('Water Consumption')

        # Food chart
        plt.subplot(1, 2, 2)
        data_food = [self.consumed_food, food_left]
        labels_food = ['Consumed Food', 'Food Left']
        plt.pie(data_food, labels=labels_food, autopct='%1.1f%%', startangle=90)
        plt.title('Food Consumption')

        plt.show()

# Example usage
if __name__ == "__main__":
    tracker = WaterTracker(20, 10)  # Assume 20 liters of water and 10 kg of food available
    tracker.consume_water(5)
    tracker.consume_food(2)
    print(f"Water left: {tracker.water_left()} liters")
    print(f"Food left: {tracker.food_left()} kg")
    print(f"Recommended water ration for 3 days in the desert: {tracker.recommend_ration(3, 'water', 'desert')} liters/day")
    print(f"Recommended food ration for 3 days: {tracker.recommend_ration(3, 'food')} kg/day")
    tracker.generate_chart()
