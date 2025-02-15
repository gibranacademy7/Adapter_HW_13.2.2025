class Hamburger:
    def __init__(self):
        self.bun = None
        self.vegetables = []
        self.main_component = None
        self.sauce = None
        self.hot_side = None
        self.packaging = None
        self.price = 0.0

    def __str__(self):
        return (f"Hamburger with {self.bun}, "
                f"Vegetables: {', '.join(self.vegetables)}, "
                f"Main Component: {self.main_component}, "
                f"Sauce: {self.sauce}, "
                f"Hot Side: {self.hot_side}, "
                f"Packaging: {self.packaging}, "
                f"Price: ${self.price:.2f}")
