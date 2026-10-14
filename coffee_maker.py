
class CoffeeMaker:
    def __init__(self, water: int = 500, beans: int = 100, milk: int = 200, waste_bin_full: bool = False):
        # initialise coffee maker with the default resources levels in ml/grams
        self.water = water
        self.beans = beans
        self.milk = milk
        self.waste_bin_full = waste_bin_full
        self.brew_count = 0
    
    def get_resources(self):
        print("-----Current Resources-----")
        print(f"Water: {self.water} ml")
        print(f"Beans: {self.beans} g")
        print(f"Milk: {self.milk} ml")
        print(f"Waster bin full: {self.waste_bin_full}")

    def check_resources(self, water_needed, beans_needed, milk_needed):
        #raise an error if any resource is too low or waste bin is full
        if self.water < water_needed:
            raise ValueError("Not enough water to brew")
        if self.beans < beans_needed:
            raise ValueError("Not enough beans to brew")
        if self.milk < milk_needed:
            raise ValueError("Not enough milk to brew")
        if self.waste_bin_full:
            raise ValueError("Waste bin is full, empty it before you brew")

    def add_water(self, amount):
        self.water = self.water + amount
    
    def add_beans(self, amount):
        self.beans = self.beans + amount

    def add_milk(self, amount):
        self.milk = self.milk + amount

    def empty_waste_bin(self):
        self.waste_bin_full = False
