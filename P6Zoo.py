class Animal:
    def __init__(self, name, type, specie, weight):
        self.name = name
        self.type = type
        self.specie = specie
        self.weight = weight
    
    def move(self):
        pass
    
    def eat(self):
        pass  
          
    def info(self):
        print(f'The name of the {self.specie} is {self.name}, {self.name} is a {self.type} and it weights {self.weight} lb')
        
class Lion(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is running')
    
    def eat(self):
        print(f'{self.name} is eating meat')
        
class Monkey(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is jumping between ropes')
    
    def eat(self):
        print(f'{self.name} is eating fleas')

class Iguana(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is running over the water')
    
    def eat(self):
        print(f'{self.name} is eating vegetables and fruits')

class Crocodile(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is swimming in the water')
    
    def eat(self):
        print(f'{self.name} is eating meat')
        
class Zebra(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is jumping in the field')
    
    def eat(self):
        print(f'{self.name} is eating grass')

class Giraffe(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is running around the field')
    
    def eat(self):
        print(f'{self.name} is eating grass from the trees')
        
class Turtle(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is sleeping in its shell')
    
    def eat(self):
        print(f'{self.name} is eating seaweed and shrimp')
        
class Hippo(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is taking a shower in the lake')
    
    def eat(self):
        print(f'{self.name} is eating lettuce')
        
class Python(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is trying to hide in its cave')
    
    def eat(self):
        print(f'{self.name} is eating meat')
        
class Tigger(Animal):
    def __init__(self, name, type, specie, weight):
        super().__init__(name, type, specie, weight)

    def move(self):
        print(f'{self.name} is running too quickly')
    
    def eat(self):
        print(f'{self.name} is eating meat')

lion = Lion('Gatito', 'Mammal', 'Lion', 600)
lion.info()
lion.move()
lion.eat()
monkey = Monkey('Lisa', 'Mammal', 'Monkey', 80)
monkey.info()
monkey.move()
monkey.eat()
iguana = Iguana('Iguanol', 'Reptile', 'Iguana', 6)
iguana.info()
iguana.move()
iguana.eat()
crocodile = Crocodile('Pancho', 'Reptile', 'Crocodile', 450)
crocodile.info()
crocodile.move()
crocodile.eat()
zebra = Zebra('Marty', 'Mammal', 'Zebra', 700)
zebra.info()
zebra.move()
zebra.eat()
giraffe = Giraffe('Melman', 'Mammal', 'Giraffe', 1000)
giraffe.info()
giraffe.move()
giraffe.eat()
turtle = Turtle('Leonardo', 'Reptile', 'Turtle', 800)
turtle.info()
turtle.move()
turtle.eat()
hippo = Hippo('Maria', 'Mammal', 'Hippo', 1800)
hippo.info()
hippo.move()
hippo.eat()
python = Python('Pedro', 'Reptile', 'Snake', 30)
python.info()
python.move()
python.eat()
tigger = Tigger('Jackson', 'Mammal', 'Tigger', 450)
tigger.info()
tigger.move()
tigger.eat()

print("hello")