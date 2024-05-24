class Animal:
    """This class represents an animal in the zoo. Each animal has attributes such as name, species, age, height, width, preferred habitat, and health."""

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str, health = None) -> None:
        """Initializes an Animal object with specified attributes.

        Attributes:
            name (str): The name of the animal.
            species (str): The species of the animal.
            age (int): The age of the animal.
            height (float): The height of the animal.
            width (float): The width of the animal.
            preferred_habitat (str): The preferred habitat of the animal.
            health (float): The health of the animal. Defaults to None because calculated inside the class.
            """
        self.name: str = name 
        self.species: str = species
        self.age: int = age 
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.size: float = self.calculate_animal_size()
        self.health: float = self.calculate_animal_health()

    def __str__(self) -> str:
        """Returns a string representation of the Animal object."""
        return f"Animal(name={self.name}, species={self.species}, age={self.age})"
    
    def calculate_animal_size(self, fed_animal: bool = None) -> float:
        """Calculates the size (area) of the animal.

        Args:
            fed_animal (bool, optional): Flag indicating whether the animal is being fed. Defaults to None.

        Returns:
            float: The size of the animal or the new size of the animal if being fed.
            """
        if fed_animal == None:
            self.size = self.height * self.width
        else:
            self.height = self.height * 1.02
            self.width = self.width * 1.02
            self.size = self.height * self.width
        return self.size

    def calculate_animal_health(self, fed_animal: bool = None) -> float:
        """Calculates the health of the animal.

        Args:
            fed_animal (bool, optional): Flag indicating whether the animal is being fed. Defaults to None.

        Returns:
            float: The health of the animal or the new health of the animal if being fed.
            """
        if fed_animal == None:
            self.health = round(100 * (1 / self.age), 3)
        else:
            self.health = self.health * 1.01
        return self.health
    

class Fence:
    """This class represents a fence in the zoo where animals are kept. Fences can contain one or more animals and have attributes such as area, temperature, and habitat."""

    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        """Initializes a Fence object with specified attributes.

        Attributes:
            area (float): The area of the fence.
            temperature (float): The temperature of the fence.
            habitat (str): The habitat of the fence.
            """
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.occupied_area: float = 0
        self.available_area: float = self.area
        self.caged_animals: list = []
    
    def __str__(self) -> str:
        """Returns a string representation of the Fence object."""
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"

    def update_occupied_area(self) -> None:
        """Updates the occupied area of the fence."""
        self.occupied_area = sum(animal.size for animal in self.caged_animals)
        self.available_area = self.area - self.occupied_area

    def get_available_area(self) -> float:
        "Shows the available area in the fence"
        return self.available_area

    def get_occupied_area(self) -> float:
        "Shows the occupied area in the fence"
        return self.occupied_area


class ZooKeeper:
    """This class represents a ZooKeeper responsible for managing the zoo. ZooKeepers have a name, surname, and ID. They can perform tasks such as feeding animals, cleaning enclosures, and other duties in the zoo."""

    def __init__(self, name: str, surname: str, id:int) -> None:
        """Initializes a ZooKeeper object with specified attributes.

        Attributes:
            name (str): The name of the ZooKeeper.
            surname (str): The surname of the ZooKeeper.
            id (int): The ID of the ZooKeeper.
            """
        self.name: str = name
        self.surname: str = surname
        self.full_name: str = name + " " + surname
        self.id: int = id
        self.tempo: float = None
        self.fence_list: list = []
    
    def __str__(self) -> str:
        """Returns a string representation of the ZooKeeper object."""
        return f"Guardian(name={self.name}, surname={self.surname}, id={self.id})"
    
    def add_fence(self, Fence: Fence) -> None:
        """Adds a fence to the ZooKeeper's list of fences to be managed.

        Args:
            Fence (Fence): The fence to be added.
            """
        self.fence_list.append(Fence)

    def pick_fence(self, Animal: Animal) -> str:
        """Chooses an available fence for the animal based on its preferred habitat.

        Args:
            Animal (Animal): The animal to be housed in the fence.

        Returns:
            str: A message indicating the selected fence or an error message.
            """    
        suitable_fence_found: bool = False
        for fence in self.fence_list:
            if Animal.preferred_habitat.lower() == fence.habitat.lower():
                print(f"{Animal.name}'s perfect habitat is in the fence with the habitat: {fence.habitat}.")
                suitable_fence_found: bool = True
                break
        if suitable_fence_found == False:
            raise ValueError(f"There is no fence with the habitat {Animal.preferred_habitat}.")
                
    def add_animal(self, Animal: Animal, Fence: Fence) -> None:
        """Adds a new animal to the zoo in an appropriate fence.

        Args:

            Animal (Animal): The animal to be added to the fence.
            Fence (Fence): The fence where the animal will be housed.
            """
        if Animal.preferred_habitat.lower() == Fence.habitat.lower():
            if Animal.size < Fence.available_area:
                Fence.caged_animals.append(Animal)
                Fence.update_occupied_area()
            else:
                raise ValueError(f"There is not enough room for the {Animal.name}. Please pick another fence.")
        else:
            raise ValueError(f"This is not the right habitat to {Animal.name}. Please pick another fence.")

    def remove_animal(self, Animal: Animal, Fence: Fence) -> None:
        """Removes an animal from the fence.

        Args:
            Animal (Animal): The animal to be removed from the fence.
            Fence (Fence): The fence from which the animal will be removed.
            """
        if Animal in Fence.caged_animals:
            Fence.caged_animals.remove(Animal)
            Fence.update_occupied_area()
        else:
            raise ValueError(f"{Animal.name} not in the fence.")

    def feed(self, Animal: Animal) -> None:
        """Feeds an animal in the zoo.

        Args:
            Animal (Animal): The animal to be fed.
            """
        animal_in_fence: bool = False
        for fence in self.fence_list:
            if Animal in fence.caged_animals:
                animal_in_fence = True
                if Animal.size * 0.02 + fence.occupied_area < fence.available_area:
                    Animal.calculate_animal_health(fed_animal=True)
                    Animal.calculate_animal_size(fed_animal=True)
                    fence.update_occupied_area()
                    animal_in_fence: bool = True
                else:
                    raise ValueError(f"{Animal.name} will be too big for this fence. Please transfer the animal to another fence before feeding it.")
                break
        if animal_in_fence == False:
            raise ValueError(f"{Animal.name} not in a fence. Please transfer the animal to a fence before feeding it.")

    def clean(self, Fence: Fence) -> float:
        """Cleans a fence in the zoo and returns the time taken.

        Args:
            Fence (Fence): The fence to be cleaned.

        Returns:
            float: The time taken to clean the fence.
            """     
        if Fence.available_area <= 0:
            return Fence.get_occupied_area()
        else:
            self.tempo: float = Fence.occupied_area / Fence.available_area
            return f"it took {self.tempo} unit of time to clean the area."
    
    def get_caged_animals(self) -> str:
        """Prints all the animals in each fence managed by the ZooKeeper."""
        print("Fences:")
        for fence in self.fence_list:
            print(fence)
            print("with animals:")
            for animal in fence.caged_animals:
                print(animal)
            print(30 * "#")


class Zoo:
    """This class represents a zoo. The zoo consists of fences and ZooKeepers."""
    
    def __init__(self, Fence_list: list[Fence], ZooKeeper_list: list[ZooKeeper]) -> None:
        """Initializes a Zoo object with specified fences and ZooKeepers.

        Attributes:
            Fence_list (list[Fence]): A list of fences in the zoo.
            ZooKeeper_list (list[ZooKeeper]): A list of ZooKeepers managing the zoo.
            """
        self.fences = Fence_list
        self.zoo_keepers = ZooKeeper_list
    
    def describe_zoo(self) -> str:
        """Prints information about all the ZooKeepers and the fences with animals."""
        print("Guardians:")
        for ZooKeeper in self.zoo_keepers:
            print(ZooKeeper)
            ZooKeeper.get_caged_animals()