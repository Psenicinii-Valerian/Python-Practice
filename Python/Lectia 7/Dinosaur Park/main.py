from abc import ABC, abstractmethod


class Dinosaur(ABC):
    age = 10230210343
    @abstractmethod
    def get_personal_name(self):
        pass

    @abstractmethod
    def get_breed(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_diet(self):
        pass

# DRY - Don't repeat yourself
class Carnivore(Dinosaur):
    def __init__(self, breed, personal_name, height, weight):
        self.breed = breed
        self.personal_name = personal_name
        self.height = height
        self.weight = weight

    def get_personal_name(self):
        return self.personal_name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_diet(self):
        return "Carnivore"

# Best Practice
# class Herbivore(Carnivore):
#     def __init__(self, breed, personal_name, height, weight):
#         super().__init__(breed, personal_name, height, weight)
#
#     def get_diet(self):
#         return "Herbivore"


class Herbivore(Dinosaur):
    def __init__(self, breed, personal_name, height, weight):
        self.breed = breed
        self.personal_name = personal_name
        self.height = height
        self.weight = weight

    def get_personal_name(self):
        return self.personal_name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_diet(self):
        return "Herbivore"


class DinosaurPark:
    def __init__(self):
        self.dinosaurs = []

    def add_dinosaur(self, dinosaur):
        self.dinosaurs.append(dinosaur)

    def list_dinosaur(self):
        # list comprehension
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), dinosaur.get_weight(),
                 dinosaur.get_height(), dinosaur.get_diet()) for dinosaur in self.dinosaurs]


t_rex = Carnivore("Tyrannosaurus Rex", "Rexy", 5, 6000)
velociraptor = Carnivore("Velociraptor", "Velic", 0.7, 20)
stegosaurus = Herbivore("Stegosaurus", "Steggy", 4, 4000)
triceratops = Herbivore("Triceratops", "Trippy", 3,10000)

park = DinosaurPark()
park.add_dinosaur(t_rex)
park.add_dinosaur(velociraptor)
park.add_dinosaur(stegosaurus)
park.add_dinosaur(triceratops)

for dinosaur in park.list_dinosaur():
    print(f"Name: {dinosaur[0]}\n"
          f"Breed: {dinosaur[1]}\n"
          f"Weight: {dinosaur[2]}kg\n"
          f"Height: {dinosaur[3]}m\n"
          f"Diet: {dinosaur[4]}\n")


