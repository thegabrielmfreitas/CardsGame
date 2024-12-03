from tkinter.font import names


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"{self.name} is {self.age} years old and is {self.height} inches tall"

    #create our getters and setters aka accessors and mutators
    # to enforce restrictions.

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value if isinstance(value, str) and len(value) >= 3 else ""


    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0 and value <= 120:
            self.age = value
        else:
            raise ValueError("Age must be between 0 and 100")

        # other option is: self.__age = value if isinstance(value, int) >= 21 else "You are bellow 21 years old"


    def run(self):
        return f"{self.name} is running!"
    def jump(self):
        return f"{self.name} is jumping!"


class SuperHero(Person):
    def __init__(self, name, age, height, super_hero_name, planet, power):
        Person.__init__(self, name, age, height)
        # super().__init__(name, age, height) --> another way to call the person
        self.planet = planet
        self.power = power
        self.super_hero_name = super_hero_name

    def fight(self, who="a bad guy"):
        return f"{self.super_hero_name} is fighting {who}!"

    def run(self):
        return f"{self.super_hero_name} is running to save the day!"

    def jump(self):
        return self.super_hero_name + super().jump().split(self.name[1])


hero = SuperHero ("Bruce Wayne", 50, 70, "Batman", "Earth", "Rich")

print(hero.fight("Joker"))
print(hero.jump())
print(hero.run())

class Lion:
    def __init__(self, name, stripes):
        self.name = name
        self.stripes = stripes

class Tiger:
    def __init__(self, teeth, weight):
        self.teeth = teeth
        self.weight = weight

class Liger(Lion, Tiger):
    pass

value = Liger("a", "b")

#Your turn: add a toString