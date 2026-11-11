from coffee_maker import CoffeeMaker

#tests the constructor
def test_default_resources():
    machine = CoffeeMaker()

    assert machine.water == 500
    assert machine.beans == 100
    assert machine.milk == 200

# test adding resources to the coffee maker
def test_add_resources():
    machine = CoffeeMaker()

    # add 150ml of water, 50g of beans, and 100ml of milk to the coffee maker
    machine.add_resources(150, 50, 100)

    # test that the resources have been updated correctly
    assert machine.water == 650
    assert machine.beans == 150 
    assert machine.milk == 300

# test successful brewing espresso
def test_brew_espresso():
    machine = CoffeeMaker()

    machine.brew_espresso()

    #check if resources have been updated correctly
    assert machine.water == 450
    assert machine.beans == 90
    assert machine.milk == 200