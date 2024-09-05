# Progetto: Realizzazione e Gestione dei Corsi ITS

print("Progetto: Realizzazione e Gestione dei Corsi ITS \n")

# Exercise 1:
""" Exercise 1: In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). L'area è calcolata come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula.

### Classe Building:
La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani (floors), e una lista di aule (rooms).
- Metodi:
    - get_floors(): Restituisce l'intervallo di piani dell'edificio.
    - get_rooms(): Restituisce la lista delle aule nell'edificio.
    - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
    - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule. """

print("Exercise 1 - Soluzione: \n")

class Room:

    def __init__(self, id: str, floor: int, seats: int) -> None:
       self.id: str = id
       self.floor: int = floor
       self.seats: int = seats
       self.area: int = 2 * self.seats

    def get_id(self) -> str:
        return self.id
     
    def get_floor(self) -> str:
        return self.floor
     
    def get_seats(self) -> str:
        return self.seats
     
    def get_area(self) -> str:
        return self.area

class Building:
   
    def __init__(self, name: str, address: str, floors: int) -> None:
       self.name: str = name
       self.address: str = address
       self.floors: int = floors
       self.rooms: list[Room] = []

    def get_rooms(self) -> str:
        return self.rooms
    
    def get_floors(self) -> str:
        return self.floors
    
    def add_room(self, room: Room) -> None:
        if room not in self.rooms:
            ground_floor, top_floor = self.floors
            if room.floor in range(ground_floor, top_floor + 1):
                self.rooms.append(room)
        return self.rooms
    
    def area(self) -> int:
        total_area: int = sum([room.area for room in self.rooms])
        return total_area

# Creazione di stanze
room1 = Room(id="Room1", floor=1, seats=15)
room2 = Room(id="Room2", floor=5, seats=20)
room3 = Room(id="Room3", floor=11, seats=10)  # Questo piano è fuori dal range

# Test classe Room
print("Test classe Room:")
print(f"ID: {room1.get_id()}, Atteso: Room1")
print(f"Piano: {room1.get_floor()}, Atteso: 1")
print(f"Posti: {room1.get_seats()}, Atteso: 15")
print(f"Area: {room1.get_area()}, Atteso: 30.0")

# Creazione di un edificio
building = Building(name="Test Building", address="123 Test St", floors=(1, 10))

# Test di inizializzazione Building
print("\nTest di inizializzazione Building:")
print(f"Nome: {building.name}, Atteso: Test Building")
print(f"Indirizzo: {building.address}, Atteso: 123 Test St")
print(f"Piani: {building.floors}, Atteso: (1, 10)")
print(f"Stanze iniziali: {building.get_rooms()}, Atteso: []")

# Test aggiunta stanza valida
building.add_room(room1)
print("\nDopo aggiunta Room1:")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test aggiunta stanza su piano non valido
building.add_room(room3)
print("\nDopo tentativo di aggiunta Room3 (piano non valido):")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test aggiunta stanza duplicata
building.add_room(room1)
print("\nDopo tentativo di aggiunta duplicato Room1:")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test calcolo area
building.add_room(room2)
print("\nDopo aggiunta Room2:")
print(f"Area totale: {building.area()}, Atteso: 70.0")

# Test rappresentazione in stringa Building
print("\nRappresentazione in stringa dell'edificio:")
print(f"Nome Edificio: {building.name}")
print(f"Indirizzo Edificio: {building.address}")
print(f"Piani Edificio: {building.get_floors()}")
print("Stanze nell'edificio:")
for room in building.get_rooms():
    print(f"ID Stanza: {room.get_id()}, Piano: {room.get_floor()}, Posti: {room.get_seats()}, Area: {room.get_area()}")
print(f"Area totale dell'edificio: {building.area()}m2")

# Verifica valori attesi
atteso_stanze = ["Room1", "Room2"]
atteso_area = 70.0
print(f"\nVerifica finale: Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: {atteso_stanze}")
print(f"Verifica finale: Area totale: {building.area()}, Atteso: {atteso_area}")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

# Exercise 2:
""" Exercise 2: Classi Person, Student e Lecturer:
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente

### Classe Group:
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti (students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. Il gruppo può avere almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto. """

print("Exercise 2 - Soluzione: \n")

class Person:

    def __init__(self, name: str, surname: str, cf: str, age: int) -> None:
        self.name: str = name
        self.surname: str = surname
        self.cf: str = cf
        self.age: int = age

class Student(Person):
    
    def __init__(self, name: str, surname: str, cf: str, age: int) -> None:
        Person.__init__(self, name, surname, cf, age)
        self.group = None

    def set_group(self, group):
        self.group = group

class Lecturer(Person):

    def __init__(self, name: str, surname: str, cf: str, age: int) -> None:
        Person.__init__(self, name, surname, cf, age)

class Group:
    
    def __init__(self, name: str, limit: int) -> None:
        self.name: str = name
        self.limit: int = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []

    def get_name(self) -> str:
        return self.name
    
    def get_limit(self) -> int:
        return self.limit
    
    def get_students(self) -> list:
        return self.students
    
    def get_limit_lecturers(self) -> int:
        max_lecturers = 1

        if len(self.students) <= 10:
            max_lecturers = 1

        elif len(self.students) > 10:
            students_decimal_counter = len(self.students)
            while len(self.students) > 10:
                max_lecturers += 1
                students_decimal_counter -= 10

        lecturers = len(self.lecturers)

        return max_lecturers - lecturers
    
    def add_student(self, student: Student):
        if len(self.students) < self.limit:
            self.students.append(student)
        return self.students

    def add_lecturer(self, lecturer: Lecturer):
        limit_lecturers = self.get_limit_lecturers()
        if limit_lecturers >= 1:
            self.lecturers.append(lecturer)
        
        return self.lecturers

# Creazione delle persone
person1 = Person(cf="CF123", name="John", surname="Doe", age=30)
student1 = Student(cf="CF456", name="Jane", surname="Smith", age=20)
lecturer1 = Lecturer(cf="CF789", name="Dr. Emily", surname="Brown", age=45)

# Test della classe Person
print("Test della classe Person:")
print(f"CF: {person1.cf}, Atteso: CF123")
print(f"Nome: {person1.name}, Atteso: John")
print(f"Cognome: {person1.surname}, Atteso: Doe")
print(f"Età: {person1.age}, Atteso: 30")

# Test della classe Student
print("\nTest della classe Student:")
print(f"CF: {student1.cf}, Atteso: CF456")
print(f"Nome: {student1.name}, Atteso: Jane")
print(f"Cognome: {student1.surname}, Atteso: Smith")
print(f"Età: {student1.age}, Atteso: 20")
print(f"Gruppo iniziale: {student1.group}, Atteso: None")

# Test metodo set_group della classe Student
group1 = Group(name="Group A", limit=10)
student1.set_group(group1)
print("\nDopo set_group di student1:")
print(f"Gruppo di student1: {student1.group.get_name()}, Atteso: Group A")

# Test della classe Lecturer
print("\nTest della classe Lecturer:")
print(f"CF: {lecturer1.cf}, Atteso: CF789")
print(f"Nome: {lecturer1.name}, Atteso: Dr. Emily")
print(f"Cognome: {lecturer1.surname}, Atteso: Brown")
print(f"Età: {lecturer1.age}, Atteso: 45")

# Creazione di un gruppo e aggiunta di studenti e docenti
group2 = Group(name="Group B", limit=2)
group2.add_student(student1)
group2.add_lecturer(lecturer1)

print("\nDopo aggiunta di student1 e lecturer1 a group2:")
print(f"Studenti in group2: {[student.cf for student in group2.get_students()]}, Atteso: [CF456]")
print(f"Docenti in group2: {[lecturer.cf for lecturer in group2.lecturers]}, Atteso: [CF789]")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

# Exercise 3:
""" Exercise 3: Classe Course:
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso. """

print("Exercise 3 - Soluzione: \n")

class Course:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.groups: list = []
    
    def register(self, student: Student):
        for group in self.groups:
            if len(group.students) < group.limit:
                group.add_student(student)
                break

    def get_groups(self):
        return self.groups
    
    def add_group(self, group: Group):
        if group not in self.groups:
            self.groups.append(group)
        
        return self.groups


# Creazione degli edifici
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

# Aggiunta delle stanze all'edificio smi
smi.add_room(Room(id="123", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
smi.add_room(Room(id="111", floor=-1, seats=32))

# Aggiunta delle stanze all'edificio smi
armellini.add_room(Room(id="567", floor=3, seats=22))
armellini.add_room(Room(id="888", floor=0, seats=32))
armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
armellini.add_room(Room(id="999", floor=2, seats=22))

# Output dei risultati
print("### SMI ###")
print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
print(f"Area totale dell'edificio SMI: {smi.area()} m²")
print("### ARMELLINI ###")
print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


# Creazione dei gruppi
fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="Cloud", limit=10)
cyber = Group(name="Cyber", limit=10)

# Creazione di un corso e aggiunta dei gruppi al corso
course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)

# Registrazione degli studenti al corso
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

print("### COURSE DETAILS ###")
print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")