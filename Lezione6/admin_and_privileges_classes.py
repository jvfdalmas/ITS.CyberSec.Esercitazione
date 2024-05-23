from user_class_file import User

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