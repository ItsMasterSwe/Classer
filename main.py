import random


class Animal:
    def __init__(self, age, name, race):
        self.name = name
        self.age = age
        self.race = race


class dog(Animal):

    def describe(self):
        print(f'Hej mitt namn är {self.name} och jag är {self.age} år gammal! Jag är en {self.race}')

    def bark(self):
        print(f'{self.name} says woof!')

    def running(self):
        print(f'Hunden springer')


dog1 = dog(12, "Oskar", 'Husky')
dog2 = dog(13, "Momo", 'Pudel')

lstDogs = []
lstDogs.append(dog1)
lstDogs.append(dog2)


def flipCoin(sannolikhet):

    randNr = random.randint(0, sannolikhet - 1)
    if randNr == 0:
        return True
    else:
        return False


for dog in lstDogs:
    if flipCoin(2):
        dog.bark()
        dog.describe()
