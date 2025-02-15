from hamburger_builder import HamburgerBuilder

def create_crispy_chicken_burger():
    builder = HamburgerBuilder()
    return (builder.add_bun("Sesame Bun")
            .add_vegetables(["Lettuce", "Tomato"])
            .add_main_component("Crispy Chicken")
            .add_sauce("Mayo")
            .add_hot_side("Fries")
            .add_packaging("Paper Wrap")
            .add_price(8.99)
            .build())

def create_beyond_burger():
    builder = HamburgerBuilder()
    return (builder.add_bun("Whole Wheat Bun")
            .add_vegetables(["Onion", "Pickles"])
            .add_main_component("Beyond Meat")
            .add_sauce("Ketchup")
            .add_hot_side("Salad")
            .add_packaging("Box")
            .add_price(9.99)
            .build())

def create_house_burger():
    builder = HamburgerBuilder()
    return (builder.add_bun("Regular Bun")
            .add_vegetables(["Cucumber", "Spinach"])
            .add_main_component("Beef Patty")
            .add_sauce("BBQ Sauce")
            .add_hot_side("Onion Rings")
            .add_packaging("Paper Box")
            .add_price(10.99)
            .build())

if __name__ == "__main__":
    crispy_chicken = create_crispy_chicken_burger()
    beyond_burger = create_beyond_burger()
    house_burger = create_house_burger()

    print(crispy_chicken)
    print(beyond_burger)
    print(house_burger)
