class Player(object):
    def __init__(self, name, level, health, xp):
        if not isinstance(name, str):
            raise ValueError("Your name needs to be a string")
        name = name + ' '
        self._player = name
        self._level = level
        self._health = health
        self._xp = xp
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return None

    def take_damage(self, damage):
        self._health -= damage

    def heal(self, amount):
        self._health += amount

    def player_attack_enemy(player, enemy):
        damage = player._level * 10  # You can adjust the damage calculation
        print("You attack the "+enemy+"slaying it")

    def enemy_attack_player(player, enemy):
        damage = enemy.damage
        player.take_damage(damage)

class Enemy(Player):
    def __init__(self, name, health):
        health = 5
        xp = 0
        super.__init__( name, level, health, xp)

class Location:
    #The constructor of the location class
    #The location class stores data on the player location and items in them areas
        def __init__(self,  description):
            self.description = description
            self.north = None
            self.south = None
            self.east = None
            self.west = None
            self.pickups = []
            self.enemies = []
    
        def add_enemy(self, enemy):
            self.enemies.append(enemy)
        
        def remove_enemy(self, enemy):
            if enemy in self.enemies:
                self.enemies.remove(enemy)

        def add_pickup(self, x):
            self.pickups.append(x)

        def remove_pickup(self, x):
            if x in self.pickups:
                self.pickups.remove(x)
                return x
            return None
    
        def show_pickups(self):
            if self.pickups:
                print("Pickups in this location ", ','.join(self.pickups))
            else:
                print("No pickups in this location.")
    


#Setup the player class
name = input("Please enter your name please ")
level = 1
xp = 0
health = 100
player = Player(name, level, xp, health)

#setup locations for the class
locations = {
    'cave': Location('a vast empty cave '),
    'forest': Location('a trail through a dark forest '),
    'mountain pass': Location('a narrow trail through the mountains '),
    'base': Location('the base of the adventurer ' + name ),
    'Goblin camp': Location('a camp filled with goblins ')
}
#link the location objects together
locations['base'].north = locations['Goblin camp']
locations['Goblin camp'].south = locations['base']
locations['base'].south = locations['mountain pass']
locations['mountain pass'].north = locations['base']
locations['base'].east = locations['forest']
locations['forest'].west = locations['base']
locations['base'].west = locations['cave']
locations['cave'].east = locations['base']

#insert enemies into the locations
locations['Goblin camp'].add_enemy('Goblin ')
locations['mountain pass'].add_enemy('bandits ')
locations['forest'].add_enemy('undead ')
locations['cave'].add_enemy('spider ')


location = locations['base']

response = ' '
while response != 'quit':
    response = input('You see '+location.description) 
    match response:
        case 'north':
            location = location.north
        case 'south':
            location = location.south
        case 'east':
            location = location.east
        case 'west':
            location = location.west
        case 'take ':
            item_to_take = response[5:]
            taken_item = location.remove_pickup(item_to_take)
            if taken_item:
                player.add_to_inventory(taken_item)
                print('Picked up ' + taken_item)
            else:
                print('Item not found.')
        case 'show inventory':
            if player.inventory:
                print("Inventory: " + ', '.join(player.inventory))
            else:
                print("Your inventory is empty.")
        case 'show pickups':
            location.show_pickups()
        case 'quit':
            response = 'quit'
        case _:
            "Invalid response please use the directional commands North,South,East,West \n or the show commands show pickups or show inventory"
    
    if location.enemies:
        enemy = location.enemies[0]
        print("You encounter an enemy!")
        choice = input("Select what to do, type 'attack' or type 'run': ")
        
        if choice == 'run':
            print("You managed to escape from the enemy!")
        elif choice == 'attack':
            Player.player_attack_enemy(player, enemy)
            location.remove_enemy(enemy)
            match isinstance(location, Location) and location.description:
                case 'a camp filled with goblins ':
                    location.description = "the camp free from goblins, what will you do? "
                case 'a vast empty cave ':
                    location.description = "the cave is free from the spiders, what will you do? "
                case 'a trail through a dark forest ':
                    location.description = "the forest no longer has an undead infestation, what will you do? "
                case 'a narrow trail through the mountains ':
                    location.description = "that you dealt with the bandits, what will you do? "
            
