from hamburger import Hamburger

class HamburgerBuilder:
    def __init__(self):
        self.hamburger = Hamburger()

    def add_bun(self, bun):
        self.hamburger.bun = bun
        return self

    def add_vegetables(self, vegetables):
        self.hamburger.vegetables.extend(vegetables)
        return self

    def add_main_component(self, component):
        self.hamburger.main_component = component
        return self

    def add_sauce(self, sauce):
        self.hamburger.sauce = sauce
        return self

    def add_hot_side(self, hot_side):
        self.hamburger.hot_side = hot_side
        return self

    def add_packaging(self, packaging):
        self.hamburger.packaging = packaging
        return self

    def add_price(self, price):
        self.hamburger.price = price
        return self

    def build(self):
        return self.hamburger
