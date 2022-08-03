class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name_of_animal):
        self.species = species
        self.name_of_animal = name_of_animal
        if species == "mammal":
            self.mammals.append(name_of_animal)
        elif species == "fish":
            self.fishes.append(name_of_animal)
        elif species == "bird":
            self.birds.append(name_of_animal)
        Zoo.__animals += 1

    def get_info(self, type):
        result = ""
        if type == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif type == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif type == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result
zoo_name = input()
animals = int(input())
zoo = Zoo(zoo_name)

for animal in range(animals):
    animal_info = input().split()
    species = animal_info[0]
    name = animal_info [1]
    zoo.add_animal(species, name)

type = input()
print(zoo.get_info(type))
