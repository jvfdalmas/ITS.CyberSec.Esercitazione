"""Creaiamo un sistema di gestione di uno zoo virtuale
Sistema di gestione dello zoo virtuale

Classi:
1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.
4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:
1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.
2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.
3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.
4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.
5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:
ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)
Fences:
Fence(area=100, temperature=25, habitat=Continent)
with animals:
Animal(name=Scoiattolo, species=Blabla, age=25)
Animal(name=Lupo, species=Lupus, age=14)
#########################
Fra un recinto e l'altro mettete 30 volte il carattere #."""

class Animal:
    """Questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3)."""

    def __init__(self, name: str, species: str, age: int, height: float, width: float) -> None:
        self.name: str = name 
        self.species: str = species
        self.age: int = age 
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = self.pick_preferred_habitat()
        self.size: float = self.calculate_animal_size()
        self.health: float = self.calculate_animal_health()

    def __str__(self) -> str:
        """This function prints the attributes in the form of a str.
        input: None
        return: str with the attributes """

        return f"name: {self.name}, species: {self.species}, age: {self.age}, health: {self.health}, height: {self.height}, width: {self.width}, size: {self.size}, preferred habitat: {self.preferred_habitat},"
    

    def calculate_animal_size(self, height: float, width: float) -> float:
        """Calculates animal's size (area)"""

        size = height * width
        return size


    def calculate_animal_health(self, age: int) -> float:
        """Calculates animal's health"""

        self.health: float = round(100 * (1 / self.age), 3)
        return self.health
    

    def pick_preferred_habitat(self, species) -> str:
        """"Chooses habitat for the animal based on its species"""
        habitat_per_specie: dict = {"lupus": "forest", "Blabla": "park"}
        self.preferred_habitat: str = ""

        if species in habitat_per_specie:
            self.preferred_habitat = habitat_per_specie[species]
        else:
            return "specie not available in the list. Please contact administrator!"

        return self.preferred_habitat




class Fence:
    """Questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat."""

    def __init__(self, area: float, temperature: float, habitat: str) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.available_area: float = None
        self.occupied_area: float = None


    def create_fence(self, area: float, habitat: str, temperature: float, occupied_area: float, available_area: float) -> None:
        """Create fence"""
    

    def describe_fences(self, fences: list) -> str:
        """Describes the fences in the Zoo"""


    def get_available_area(self) -> float:
        "Shows the available area in the fence"
        return self.available_area


    def get_occupied_area(self) -> float:
        "Shows the occupied area in the fence"
        return self.occupied_area


    def pick_fence(self, Animal: Animal, preferred_habitat: str, Fence_list: list) -> str:
        """"Chooses available fence for the animal based on the preferred_habitat"""
        
        habitat_per_preferred_habitat: dict = {"forest": "forest", "park": "park"}
                    


class Zookeper:
    """Questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale."""

    def __init__(self, name: str, surname: str, id:int) -> None:
        self.name: str = name
        self.surname: str = surname
        self.full_name: str = name + " " + surname
        self.id: int = id
        self.tempo: float = None
    

    def create_zookeeper(self, full_name: str, id: int) -> None:
        """Creates a zookepper"""
    

    def add_animal(self, Animal: Animal, Fence: Fence):
        """Consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale."""


    def remove_animal(self, Animal: Animal, Fence: Fence):
        """Consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava."""
    

    def feed(self, Animal: Animal, Fence: Fence):
        """Consete al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo."""


    def clean(self, Fence: Fence) -> float:
        """Consente al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata."""
        
        if Fence.available_area <= 0:
            return Fence.occupied_area
        else:
            self.tempo: float = Fence.occupied_area / Fence.available_area
            return self.tempo



class Zoo:
    """Questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers."""

    def __init__(self, Fence_list: list[Fence], Zookeeper_list: list[Zookeper]) -> None:
        self.fences = Fence_list
        self.zoo_keepers = Zookeeper_list
    

    def describe_zoo (self):
        """Visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali."""

zookeper_list: list[Zookeper] = []
fence_list: list[Fence] = []
animals_list: list[Animal] = []

