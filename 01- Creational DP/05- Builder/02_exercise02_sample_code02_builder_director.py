class House:
    def __init__(self):
        self.floor = None
        self.wall = None
        self.roof = None
        self.furniture = {}

    def __str__(self):
        return (
            f"Floor: {self.floor}\n"
            f"Wall: {self.wall}\n"
            f"Roof: {self.roof}\n"
            f"Furniture: {self.furniture}\n"
        )


# creating instnaces of House
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def set_floor(self, amount):
        self.house.floor = amount

    def set_wall(self, amount):
        self.house.wall = amount

    def set_roof(self, amount):
        self.house.roof = amount
        # no need to return self again using this process

    def set_furniture(self, name, amount):
        if not self.house.furniture.get(name):
            self.house.furniture[name] = 0
        self.house.furniture[name] += amount

    def get_house(self):
        return self.house


# Type of Houses
# concrete class
# build the couse
# no need to return self HouseBuilder as
# chaning is already defined SmallHouseBuilder
class SmallHouseBuilder(HouseBuilder):
    def build_floor(self):
        self.set_floor("Small floor")

    def build_wall(self):
        self.set_wall("Small wall")

    def build_roof(self):
        self.set_roof("Small roof")

    def build_furnitures(self):
        self.set_furniture("Chairs", 5)
        self.set_furniture("Chairs", 4)
        self.set_furniture("Tables", 8)


class BigHouseBuilder(HouseBuilder):
    def build_floor(self):
        self.set_floor("Big floor")

    def build_wall(self):
        self.set_wall("Big wall")

    def build_roof(self):
        self.set_roof("Big roof")

    def build_furnitures(self):
        self.set_furniture("Sofa", 30)
        self.set_furniture("Cabinets", 28)
        self.set_furniture("Stools", 34)
        self.set_furniture("Leg Rest", 27)


# director class how construction process orchasted
class Contractor:  # director
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        # build house according to it
        # take building house
        # building order is important
        # chaning is defined here
        # construction in specific patterns
        self.builder.build_floor()
        self.builder.build_wall()
        self.builder.build_roof()
        self.builder.build_furnitures()


# usage
if __name__ == "__main__":
    # concrete class
    small_builder = SmallHouseBuilder()
    big_builder = BigHouseBuilder()

    contractor = Contractor(small_builder)
    # set all attribute of house objects
    contractor.construct_house()
    # get constructed House objects
    small_house = small_builder.get_house()
    print("Small House:")
    print(small_house)

    contractor = Contractor(big_builder)
    contractor.construct_house()
    big_house = big_builder.get_house()
    print("Big House:")
    print(big_house)

    """
    Note:
    Use any of process as prev example shows or this
    depend on use case
    """
