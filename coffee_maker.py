
class CoffeeMaker:
    def __init__(self, water:int = 500, beans:int = 100, milk:int = 200):
        # initialise coffee maker with the default resources levels in ml/grams
        self.water = water
        self.beans = beans
        self.milk = milk
    
    # brew an espresso and update resources
    def brew_espresso(self):
        if self.water >= 50 and self.beans >= 10:
            self.water -= 50
            self.beans -= 10
            print("Espresso brewed successfully")
        else:
            print("Not enough resources to brew espresso")

    # brew a latte and update resources
    def brew_latte(self):
        if self.water >= 200 and self.beans >= 20 and self.milk >= 150:
            self.water -= 200
            self.beans -= 20
            self.milk -= 150
            print("Latte brewed successfully")
        else:
            print("Not enough resources to brew latte")
