from coffee_maker import CoffeeMaker

def test_default_resources():
    machine = CoffeeMaker()

    assert machine.water == 500
    assert machine.beans == 100
    assert machine.milk == 200

def test_add_water():
    machine = CoffeeMaker()
    
    machine.add_water(150)
    
    assert machine.water == 650