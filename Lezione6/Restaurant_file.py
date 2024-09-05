class Restaurant:
    
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name: str = restaurant_name
        self.cuisine_type: str = cuisine_type
        self.number_served: int = 0

    def describe_restaurant(self) -> str:
        return f"The restaurant {self.restaurant_name} is {self.cuisine_type} cuscine."
    
    def open_restaurant(self) -> str:
        return f"The restaurant {self.restaurant_name} is open!!!"
    
    def set_number_served(self, new_number_served: int) -> None:
        self.number_served = new_number_served
    
    def increment_number_served(self, served_in_a_day: int) -> None:
        self.number_served += served_in_a_day