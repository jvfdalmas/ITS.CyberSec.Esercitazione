def make_car(manufacturer: str, car_model: str, **kwargs: dict) -> dict:
    """ Function that stores information about a car in a dictionary. Function should always receive a manufacturer and a model name and accepts an arbitrary number of dictionary arguments."""
    risult: dict = {"car model": car_model, "manufacturer": manufacturer}
    risult.update(kwargs)
    return risult
