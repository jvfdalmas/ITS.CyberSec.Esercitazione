class User:

    def __init__(self, first_name: str, last_name: str, birthday: str, birth_city: str, ) -> None:
        self.first_name:str = first_name
        self.last_name: str = last_name
        self.birthday: str = birthday
        self.birth_city: str = birth_city
        self.login_attempt: int = 0

    def describe_user(self):
        return f"user\'s name: {self.first_name} {self.last_name}, city: {self.birth_city}, birhtday: {self.birthday}"
    
    def greet_user(self):
        return f"Hello, Mr(s). {self.last_name}!"
    
    def increment_login_attempt(self) -> None:
        self.login_attempt += 1