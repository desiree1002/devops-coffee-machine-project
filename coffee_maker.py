
class CoffeeMaker:
    def __init__(self, water: int = 500, beans: int = 100, milk: int = 200):
        # initialise coffee maker with the default resources levels in ml/grams
        self.water = water
        self.beans = beans
        self.milk = milk
    
    def get_resources(self):
        print("-----Current Resources-----")
        print(f"Water: {self.water} ml")
        print(f"Beans: {self.beans} g")
        print(f"Milk: {self.milk} ml")

    def add_water(self, amount):
        self.water = self.water + amount
    
    def add_beans(self, amount):
        self.beans = self.beans + amount

    def add_milk(self, amount):
        self.milk = self.milk + amount

