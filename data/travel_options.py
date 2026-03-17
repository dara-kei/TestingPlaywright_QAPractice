import enum


class Places(enum.Enum):
    """ It is used in selects multiple testing"""

    SEA = "Sea"
    MOUNTAINS = "Mountains"
    OLD_TOWN = "Old town"
    OCEAN = "Ocean"
    RESTAURANT = "Restaurant"


class Transport(enum.Enum):
    """ It is used in selects multiple testing"""

    CAR = "Car"
    BUS = "Bus"
    TRAIN = "Train"
    AIR = "Air"


class Date(enum.Enum):
    """ It is used in selects multiple testing"""

    TODAY = "Today"
    TOMORROW = "Tomorrow"
    NEXT_WEEK = "Next week"

