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


class Admin(User):

    def __init__(self, first_name: str, last_name: str, birthday: str, birth_city: str, privileges, admin:bool = True) -> None:
        super().__init__(first_name, last_name, birthday, birth_city)
        self.admin = admin
        self.priviliges = privileges
    

class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges = privileges
    
    def show_privileges(self):
        str_privileges = ", ".join(self.privileges)
        return f"This admin has the following privileges: {str_privileges}"