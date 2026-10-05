class GardenError(Exception):
    def __init__(self, msg="Unknown garden error"):
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg="Unknown garden error"):
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg="Unknown garden error"):
        super().__init__(msg)


def test_plant_err() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print("Caught PlantError:", e)


def test_water_err() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print("Caught WaterError:", e)


def test_plant_err_as_garden() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print("Caught GardenError:", e)


def test_water_err_as_garden() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print("Caught GardenError:", e)


print("=== Custom Garden Errors Demo ===")
print()
print("Testing PlantError...")
test_plant_err()
print()
print("Testing WaterError...")
test_water_err()
print()
print("Testing catching all garden errors...")
test_plant_err_as_garden()
test_water_err_as_garden()
print()
print("All custom error types work correctly!")
