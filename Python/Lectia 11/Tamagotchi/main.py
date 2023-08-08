import random

class Tamagotchi:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        # ctrl + ctrl + sageata jos/sus pentru a selecta mai multe randuri
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)

    def feed(self):
        print(f"{self.name} is being fed")
        self.hunger -= 2
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        print(f"{self.name} is playing")
        self.energy -= 3
        if self.energy < 0:
            self.energy = 0

    def sleep(self):
        print(f"{self.name} is sleeping")
        self.energy += 5
        if self.energy > 10:
            self.energy = 10

    def __str__(self):
        return f"{self.name} ({self.species}) - Hunger: {self.hunger}, Energy: {self.energy}"

def speak(message):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"{self.name} says: {message}")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


class TalkingTamagochi(Tamagotchi):
    @speak(message="Pasiba batea za havcik")
    def feed(self):
        super().feed()

    @speak(message="Bai da tu nu ma prinzi")
    def play(self):
        super().play()

    @speak(message="Hai eu la culcare bb")
    def sleep(self):
        super().sleep()


zverushki = [Tamagotchi("Paiton", "Boa Constrictor"),
             Tamagotchi("Akira", "Doberman"),
             TalkingTamagochi("Roma", "Budgerigar")]

for zverushka in zverushki:
    print(zverushka)
    zverushka.feed()
    zverushka.play()
    zverushka.sleep()
    print(zverushka)
    print()