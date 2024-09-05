# Esercizi su classi astratte, class methods e static methods

from abc import ABC, abstractmethod

print("Esercizi su classi astratte, class methods e static methods \n")

# Exercise 1: Creating an Abstract Class with Abstract Methods
""" Exercise 1: Create an abstract class Shape with an abstract method area and another abstract method perimeter. Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods."""

print("Exercise 1 - Soluzione: \n")

class Shape(ABC):

    def __init__(self):
        pass
    
    @abstractmethod 
    def area(self):
        pass
    
    @abstractmethod 
    def permieter(self):
        pass


class Circle(Shape):

    def __init__(self, radius: float):
        Shape.__init__(self)
        self.radius = radius

    def area(self) -> float:
        return round((3.14 * self.radius ** 2), 2)
    
    def permieter(self) -> float:
        return round((2 * 3.14 * self.radius), 2)


class Rectangle(Shape):

    def __init__(self, length: float, width: float):
        Shape.__init__(self)
        self.length: float = length
        self. width: float = width

    def area(self) -> float:
        return self.length * self.width
    
    def permieter(self) -> float:
        return 2 * (self.length + self.width)


rectangle1: Rectangle = Rectangle(10, 20)
circle1: Circle = Circle(20)

print("the area of the rectangle is: ", rectangle1.area())
print("the perimeter of the rectangle is: ", rectangle1.permieter())

print("the area of the circle is: ",circle1.area())
print("the perimeter of the circle is: ", circle1.permieter())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 
# Exercise 2: Implementing Static Methods
"""Exercise 2: Create a class MathOperations with a static method add that takes two numbers and returns their sum, and another static method multiply that takes two numbers and returns their product."""

print("Exercise 2 - Soluzione: \n")

class MathOperations:

    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y
    
    @staticmethod
    def multiply(x: float, y: float) -> float:
        return x*y
    

summ = MathOperations.add(8, 10)
multip = MathOperations.multiply(8, 10)

print(f"the summ of 8 and 10 is {summ}, and the multiplication is {multip}")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 
# Exercise 3: Library Management Systems
"""Exercise 3: Create a Book class containing the following attributes: title, author, isbn.

The book class must contains the following methods:

    __str__ method to return a string representation of the book.

    @classmethod from_string(cls, book_str) to create a Book instance from a string in the format "title, author, isbn". It means that you must use the class reference cls to create a new object of the Book class using a string.

Example: 

book = “La Divina Commedia, D. Alighieri, 999000666”
divina_commedia: Book = Book.from_string(book)
Here divina_commedia must contain an instance of the class Book with 

title = La Divina Commedia, author = D. Alighieri, isbn = 999000666

Create a Member class with the following attributes: name, member_id, borrowed_books
The member class must contain the following methods:

    borrow_book(book) to add a book to the borrowed_books list.

    return_book(book) to remove a book from the borrowed_books list.

    __str__ method to return a string representation of the member.

    @classmethod from_string(cls, member_str) to create a Member instance from a string in the format "name, member_id".

Create a Library class with the following attributes: books, members, total_books (class attribute to keep track of the total number of books)
The library class must contain the following methods:

    add_book(book) to add a book to the library and increment total_books.

    remove_book(book) to remove a book from the library and decrement total_books.

    register_member(member) to add a member to the library.

    lend_book(book, member) to lend a book to a member. It should check if the book is available and if the member is registered.

    __str__ method to return a string representation of the library with the list of books and members.

    @classmethod library_statistics(cls) to print the total number of books.

Create a script and play a bit with the classes:
Create instances of books and members using class methods. Register members and add books to the library. Lend books to members and display the state of the library before and after lending."""

print("Exercise 3 - Soluzione: \n")

class Book:

    title: str = ""
    author: str = ""
    isbn: str = ""

    def __str__(self):
        return f"book: {self.title}, author: {self.author}, ISBN: {self.isbn}"

    @classmethod
    def from_string(cls, book_str):
        title, author, isbn = book_str.split(",")
        book = cls()  # Create a new instance of the Book class
        book.title = title
        book.author = author
        book.isbn = isbn
        return book


class Member:
    name = ""
    member_id = ""
    borrowed_books = []

    @classmethod
    def from_string(cls, member_str) -> None:
        name, member_id = member_str.split(",")
        member = cls()
        member.name = name
        member.member_id = member_id

        return member
    
    def __str__(self):
        books_title = [book.title for book in self.borrowed_books]
        return f"member\'s name: {self.name}, member\'s id: {self.member_id}, book\'s borrowed: {books_title}"
        
    def borrow_book(self, book: Book) -> None:
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            return self.borrowed_books
        else:
            raise ValueError ("Book already in the borrowed book\'s list")
        
    def return_book(self, book: Book) -> None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return self.borrowed_books
        else:
            raise ValueError ("Book NOT in the borrowed book\'s list")


class Library(ABC):
    books = []
    members = []

    @property
    def total_books(self):
        return len(self.books)
    
    @classmethod
    def library_statistics(cls):
        return f" total number of books: {len(cls.books)}"

    def __str__(self):
        members_list: list = [member.name for member in self.members]
        books_list: list = [book.title for book in self.books]

        return f"registered books: {books_list}, registered members: {members_list}, total number of books: {self.total_books}"

    def add_book(self, book: Book) -> None:
        if book not in self.books:
            self.books.append(book)
            return self.books
        else:
            raise ValueError ("Book already in the book\'s list")
        
    def remove_book(self, book: Book) -> None:
        if book in self.books:
            self.books.remove(book)
            return self.books
        else:
            raise ValueError ("Book NOT in the book\'s list")
    
    def register_member(self, member) -> None:
        if member not in self.members:
            self.members.append(member)
            return self.members
        else:
            raise ValueError("member already registered")
        
    def lend_book(self, book: Book, member: Member) -> None:
        if member in self.members:
            if book in self.books:
                if book not in member.borrowed_books:
                    member.borrow_book(book)
                else:
                    raise ValueError ("Book already in the borrowed book\'s list")
            else:
                raise ValueError ("Book does not exist")
        else:
            raise ValueError ("member not registered")
        
    def return_book(self, book: Book, member: Member) -> None:
        if member in self.members:
            if book in self.books:
                if book in member.borrowed_books:
                    member.return_book(book)
                else:
                    raise ValueError ("Book already NOT in the borrowed book\'s list")
            else:
                raise ValueError ("Book does not exist")
        else:
            raise ValueError ("member not registered")


book = "La Divina Commedia, D. Alighieri, 999000666"
divina_commedia: Book = Book.from_string(book)
print(divina_commedia)

book = "Dom Casmurro, Machado de Assis, 666000999"
dom_casmurro: Book = Book.from_string(book)
print(dom_casmurro)

member: str = "Joao F, JOF2050"
joao: Member = Member.from_string(member)
print(joao)

library: Library = Library()
library.add_book(divina_commedia)
library.add_book(dom_casmurro)
library.register_member(joao)
print(library)
print(library.library_statistics())

library.lend_book(divina_commedia, joao)
print(joao)
library.return_book(divina_commedia, joao)
print(joao)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 
# Exercise 4: University Management System
"""Exercise 4: Create a system to manage a university with departments, courses, professors, and students. 

Create an abstract class Person:
Attributes:

    name (string)
    age (int)

Methods:

    __init__ method to initialize the attributes.
    Abstract method get_role to be implemented by subclasses.
    __str__ method to return a string representation of the person.

Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

Student:
Additional attributes: student_id (string), courses (list of Course instances)
Method enroll(course) to enroll the student in a course.
Professor:
Additional attributes: professor_id (string), department (string), courses (list of Course instances)
Method assign_to_course(course) to assign the professor to a course.

Create a class Course:
Attributes:
    course_name (string)
    course_code (string)
    students (list of Student instances)
    professor (Professor instance)

Methods:
    __init__ method to initialize the attributes.
    add_student(student) to add a student to the course.
    set_professor(professor) to set the professor for the course.
    __str__ method to return a string representation of the course.

Create a class Department:

Attributes:
    department_name (string)
    courses (list of Course instances)
    professors (list of Professor instances)


Methods:
    __init__ method to initialize the attributes.
    add_course(course) to add a course to the department.
    add_professor(professor) to add a professor to the department.
    __str__ method to return a string representation of the department.

Create a class University:

Attributes:
    name (string)
    departments (list of Department instances)
    students (list of Student instances)


Methods:
    __init__ method to initialize the attributes.
    add_department(department) to add a department to the university.
    add_student(student) to add a student to the university.
    __str__ method to return a string representation of the university.

Create a script:

Create instances of departments, courses, professors, and students.
Add them to the university.
Enroll students in courses and assign professors to courses.
Display the state of the university."""

print("Exercise 4 - Soluzione: \n")

class Person(ABC):

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"name: {self.name}, age: {self.age}."


class Student(Person):

    def __init__(self, name: str, age: int, student_id: str):
        Person.__init__(self, name, age)
        self.student_id: str = student_id
        self.courses: list[Course] = []

    def get_role(self):
        return "student"
    
    def enroll(self, course: str) -> list[str]:
        self.courses.append(course)
        return self.courses

    def __str__(self):
        courses_list: list[str] = [course.course_name for course in self.courses]
        return f"name: {self.name}, age: {self.age}, id: {self.student_id}, course: {courses_list}"


class Professor(Person):

    def __init__(self, name: str, age: int, professor_id: str, department: str):
        Person.__init__(self, name, age)
        self.professor_id: str = professor_id
        self.department: str = department
        self.courses: list[Course] = []

    def get_role(self):
        return "professor"
    
    def assign_to_course(self, course: str) -> list[str]:
        self.courses.append(course)
        return self.courses

    def __str__(self):
        courses_list: list[str] = [course.course_name for course in self.courses]
        return f"name: {self.name}, age: {self.age}, id: {self.professor_id}, department: {self.department}, course: {courses_list}"


class Course:

    def __init__(self, course_name: str, course_code: str) -> None:
        self.course_name: str = course_name
        self.course_code: str = course_code
        self.professor: Professor = Professor
        self.students: list[Student] = []

    def add_student(self, student: Student) -> list[Student]:
        if student not in self.students:
            self.students.append(student)
        return self.students
    
    def set_professor(self, professor: Professor) -> Professor:
        if self.professor != professor:
            self.professor = professor
        return professor
    
    def __str__(self) -> str:
        students_list: list[str] = [student.name for student in self.students]
        return f"course name: {self.course_name}, course code: {self.course_code}, professor: {self.professor}, students: {"".join(students_list)}."
    

class University:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.courses: list[str] = []
        self.students: list[Student] = []
    
    def add_deparment(self, course: Course) -> list[str]:
        if course not in self.courses:
            self.courses.append(course)
        return self.courses
    
    def add_student(self, student: Student) -> list[str]:
        if student not in self.students:
            self.students.append(student)
        return self.students
    
    def __str__(self):
        students_list: list[str] = [student.name for student in self.students]
        return f"Universisty: {self.name}, departments: {self.courses}, students: {"".join(students_list)}."