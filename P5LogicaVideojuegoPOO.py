class Player:
    def __init__(self, name, strength, intelligence, defense, hp, level):
       self.name = name
       self.strength = strength
       self.intelligence = intelligence
       self.defense = defense
       self.hp = hp
       self.level = level
       
    def attributes(self):
        print('\n-Name:', self.name, f'({self.level})')
        print('-Strength:', self.strength)
        print('-Intelligence:', self.intelligence)
        print('-Defense:', self.defense)
        print('-HP:', self.hp)
        
    def levelUp(self):
        self.strength = self.strength + 3 * self.level
        self.intelligence = self.intelligence + 1 * self.level
        self.defense = self.defense + 2 * self.level
        self.hp = self.hp + 1 * self.level
        
    def aliveDead(self):
        if(self.hp > 0):
            print('Your HP is:', self.hp)
    
    def damage(self, enemy):
        return self.strength - enemy.defense
    
    def atack(self, enemy):
        damage = self.damage(enemy)
        enemy.hp = enemy.hp - damage
        print(f'\n{self.name}', 'has damaged', damage, 'points to', enemy.name)
        if(enemy.hp > 0):
            print("The", enemy.name, "HP is", enemy.hp)
        else:
            print(enemy.name, 'has died')
            
class Warrior(Player):
    
    def __init__(self, name, strength, intelligence, defense, hp, level, weapon):
        super().__init__(name, strength, intelligence, defense, hp, level)
        self.weapon = weapon
        
    def attributes(self):
        super().attributes()
        print("-Weapon damage:", self.weapon)
        
    def damage(self, enemy):
        return self.strength * self.weapon - enemy.defense
    
class Ninja(Player):
    
    def __init__(self, name, strength, intelligence, defense, hp, level, weapon):
        super().__init__(name, strength, intelligence, defense, hp, level)
        self.weapon = weapon
        
    def attributes(self):
        super().attributes()
        print("-Weapon damage:", self.weapon)
        
    def damage(self, enemy):
        return self.strength * self.weapon - enemy.defense
    
class Wizzard(Player):
    
    def __init__(self, name, strength, intelligence, defense, hp, level, weapon):
        super().__init__(name, strength, intelligence, defense, hp, level)
        self.weapon = weapon
        
    def attributes(self):
        super().attributes()
        print("-Weapon damage:", self.weapon)
        
    def damage(self, enemy):
        return self.intelligence * self.weapon - enemy.defense

#miPersonaje = Player("El Crack", 10, 5, 8, 100, 10)
#enemy = Player("Enemy", 10, 5, 8, 100, 8)
#miPersonaje.levelUp()
#miPersonaje.attributes()
#enemy.levelUp()
#enemy.attributes()
#miPersonaje.atack(enemy)
#enemy.atack(miPersonaje)
guerrero = Warrior("Guerrero", 10, 5, 8, 100, 2, 2)
ninja = Ninja("Ninja", 8, 5, 9, 100, 4, 3)
mago = Wizzard("Mago", 3, 10, 8, 100, 2, 3)
guerrero.levelUp()
guerrero.attributes()
ninja.levelUp()
ninja.attributes()
mago.levelUp()
mago.attributes()
guerrero.atack(ninja)
ninja.atack(mago)
mago.atack(guerrero)
           