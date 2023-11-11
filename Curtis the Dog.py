import pickle
import random
all_rooms = []
all_enemies = []
character_list = []
all_scharacters = []
fight = False
play = True

class character():
    def __init__ (self, name, health, strength, luck, x, y):
        self.name = name
        self.health = health
        self.strength = strength
        self.luck = luck
        self.x = x
        self.y = y
        self.level = 0
        self.points = 0
        self.currentRoom = all_rooms[x][y]
        self.inventory = []
        
    def attack(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2
        attack_value = total + self.strength
        print("dice 1: %d \nDice 2: %d \nGiving a total of %d \nWith added strength, the total is %d" %(dice1, dice2, total, attack_value))
        return attack_value
        
    def defend(self):
        return "%s has defended against the attack!"
        
    def pick_up_item(self, item):
        self.inventory.append(item)
        return self.inventory
        
    def get_name(self):
        return self.name
        
    def change_points(self, points):
        self.points = self.points + points
        return self.points
        
    def change_strength(self, points):
        self.strength = self.strength + points
        return self.strength
        
    def show_inventory(self):
        print("\nThese items are in your inventory: ")
        for x in self.inventory:
            print(x)
        return "These may be useful later..."
    
    def change_health(self, points):
        self.health = self.health - points
        return self.health        
        
    def __str__ (self):
        return "%s has %d health, %d luck and %d strength" %(self.name, self.health, self.luck, self.strength)
        
class special_character(character):
    def __init__ (self, name, description, x, y):
        character.__init__(self, name, 0, 10000, 0, x, y)
        self.description = description
        self.currentRoom = all_rooms[x][y]
        
    def power_up(self, new_character):
        luck = new_character.luck
        if luck <= 5:
            return "%s happily smiled at you" %(self.name)
        else:
            chance = random.randint(1, self.strength)
            print("%s slowly opens their mouth to reveal a gold coin" %(self.name))
            return chance 
            
        
    def __str__(self):
        return self.description
            
        

class room():
    def __init__(self, name, items, exits, description):
        self.name = name
        self.items = items
        self.exits = exits
        self.description = description
        self.enemies = []
        self.scharacters = []
        
    def show_items(self):
        return self.items
        
    def remove_items(self, item):
        if item in self.items:
            self.items.remove(item)
            print("Test: item has been removed")
            return self.items
        else:
            return "%s isn't in this room" %(item)
            
    def add_room_items(self, items, points):
        for x in items:
            self.items.append(x)
        self.items.append(points)
        return self.items
            
    def spawn_enemy(self):
        for x in range(len(all_rooms)):
            for y in range(len(all_rooms[x])):
                if all_rooms[x][y] != "":
                    if all_rooms[x][y].description == self.description: #-- doesn't work with loading rooms
                        for z in all_enemies:
                            if z.x == x and z.y == y:
                                self.enemies.append(z)

    def check_scharacter(self):
        for x in range(len(all_rooms)):
            for y in range(len(all_rooms[x])):
                if all_rooms[x][y] != "":
                    if all_rooms[x][y].description == self.description:
                        for z in all_scharacters:
                            if z.x == x and z.y == y:
                                self.scharacters.append(z)
          
    def __str__(self):
        return self.description
        
def create_rooms():
    global all_rooms
    
    room1_items = [["book"],
                   [5]]
                   
    room2_items = [["can"],
                   [10]]

    room3_items = [["box"],
                   []]                
                   
    room5_items = [["wrapper", "cup"],
                   [5, 5]]
                    
    room1 = room("A Dark Room", room1_items, ["north"], "A Dark Room \nYou find yourself stood in a room with no light source \nLooking around more you can see a dim light to the north of you \nand on the floor are some books")
    room2 = room("Hallway", room2_items, ["south", "east", "hidden"], "Hallway \nYou enter a much brighter scene, but theres not much around here \nThere are a few empty drink cans on the floor with a door slightly open towards the east \nthough it does look creepy...")
    room3 = room("the place you shouldn't have gone into", room3_items, ["west", "north"], "The place you shouldn't have gone into \nAs you look around you can see a box full of various things \nand a few doors with one open towards the north")
    room4 = room("Back Room", [], ["south"], "You have enetered the back room \nThe room is basically empty but with a single dog sat smiling at the back")
    room5 = room("Kichen", room5_items, ["south", "north"], "The Kitchen \nAs you look around there isn'anything useful left in here \nthere are a few dirty cups and chocolate wrappers scattered around \nbut to the north you can see an exit!")   
    
    all_rooms = [[room1, room2, room4],
                 ["", room3, room5]]
    
def create_enemies():
    global all_enemies
    enemy = character("Strong Enemy", 10 ,2 , 1, 1, 1)
    
    all_enemies.append(enemy)
    
def create_scharacters():
    global all_scharacters
    dog = special_character("Curtis", "Little Dog \nThis white, fluff and cute dog looks up at you smiling, \nas you check the collar the name reads 'Curtis'", 0, 2)

    all_scharacters.append(dog)

def main_menu():
    global character_list
    menu = "1. Create Character \n2. Load your character (doesnt work) \n9. Quit \n:"
    mainloop = True
    while mainloop == True:
        choice = input(menu)
        if choice == "1":
            new_character = create_character()
            if character != "":
                print("Welcome to the game", new_character.name)
                print(new_character)
                print("You can exit and save the game at any point by typing 'quit'\n")
                character_list.append(new_character)
                mainloop = False
                start_game(new_character)
            else:
                print("Unsuccessful character creation")
                
        if choice == "2":
            load_character()
            #print(character_list)
            name = input("Enter your name: ") .title()
            for x in character_list:
                if x.name == name:
                    loaded_character = x
                    #position = character_list.index(loaded_character)
                    #load_character_room(position)
                    print("Welcome back %s!" %(name))
                    create_rooms()
                    #print(all_rooms)
                    mainloop = False
                    start_game(loaded_character)
                else:
                    print("Your name isn't saved \n%s" %(menu))
                                   
        elif choice == "9":
            mainloop = False
        else:
            print("Invalid input")
            
        
            
def create_character():
    create_rooms()
    create_enemies()
    create_scharacters()
    name = input("Enter your name: ") .title()
    strength = random.randint(1, 20)
    luck = random.randint(1, 20)
    character1 = character(name, 20, strength, luck, 0, 0)
    return character1
    
def sentence_parsing(passedString, new_character, enemy):
    global all_rooms
    global all_scharacters
    global fight
    global play
    theString = passedString.split()
    
    for x in theString:
        if x == "pickup":
            if fight == False:
                item = False
                items_and_points = new_character.currentRoom.items
                items = items_and_points[0]
                points = items_and_points[1]
                for y in theString:
                    for z in items:
                        if y == z:
                            item = True
                            if z in new_character.inventory:
                                return "You already have a %s in your inventory" %(z)
                            if z == "box":
                                print("\nYou tried to pick up the box, but the box is too heavy to carry \nThen you look inside and you can see:")
                                new_items = [["headphones", "drum-stick", "another-book", "sponge"],
                                             [20,20,20,1]]
                                items2 = new_items[0]
                                points = new_items[1]
                                new_character.currentRoom.items.remove(new_character.currentRoom.items[0])
                                new_character.currentRoom.items.remove(new_character.currentRoom.items[0])
                                new_character.currentRoom.items.append(items2)
                                new_character.currentRoom.items.append(points)
                                for x in new_character.currentRoom.items[0]:
                                    print(x)
                                return "These items can now be picked up"    
                                    
                                     
                            new_character.pick_up_item(z)
                            points = get_points(z, points, items)
                            new_character.currentRoom.remove_items(z)
                            new_character.change_points(points)
                            
                            if z == "can":
                                new_character.currentRoom.exits.append("north")
                                new_character.currentRoom.exits.remove("hidden")
                                return "You have picked up a %s! \nThis gained you %s experiance points \nBut as you move it out of its place, a new exit to the north appears!" %(z, points)
                            elif z == "book":
                                desc = "As you open this book, you expect to see some sort of information \n... \nit's completely blank...\n"
                            elif z == "headphones":
                                desc = "They look pretty new! \nbut i don't think these would be of any use to you...\n"
                            elif z == "sponge":
                                desc = "...\n"
                            elif z == "another-book":
                                desc = "maybe there is something inside this book- \n... \nYou are, again, dissapointed\n"    
                            else:
                                desc = ""
                            return "%sYou have picked up a %s! \nThis gained you %s experiance points" %(desc, z, points)
                if item == False:
                    return "You can't pickup a %s"%(y)
                            
            elif fight == True:
                print("As you tried to reach for the item, the enemy attacks!")
                return enemy_only_attack(new_character, enemy)
                
                
        if x == "move" or x == "go":
	#next time, this should be written as a method inside the character class
            if fight == False:
                for y in theString:
                    for z in new_character.currentRoom.exits:
                        if y == z:
                            if z == "north":
                                if new_character.x == 1 and new_character.y == 2:
                                    if "key" in new_character.inventory:
                                        play = False
                                        return "You carefully take out the key that the cute dog gave you, \nyou then try to insert it into the lock \n...\n... \nIt works! \n\n--You Win!--\nPoints gained: %d" %(new_character.points) 
                                    else:
                                        return "As you try to open the door, you realise that a key is needed"                                    
                                else:
                                    new_character.y += 1
                            elif z == "south":
                                new_character.y -= 1
                            elif z == "east":
                                new_character.x += 1
                            elif z == "west":
                                new_character.x -= 1
                            new_character.currentRoom = all_rooms[new_character.x][new_character.y]
                            #print("TEST- coordinates are: %d,%d" %(new_character.x, new_character.y))
                            return new_character.currentRoom
                            
                        #else:
                            #return "There are no exits in that direction"
            elif fight == True:
                print("\nAs you try to get to the exit, %s stops you and attempts to attack" %(enemy.name))
                return enemy_only_attack(new_character, enemy)
        
        if x == "attack" or x == "hit":
            if fight == True:
                return battle(new_character, enemy)
            elif fight == False:
                return "There is no need to fight anyone here..."
                
        if x == "run":
            if fight == True:
                if new_character.luck >= 10:
                    print("You successfully escaped the room\n")
                    new_character.x -= 1
                    new_character.currentRoom = all_rooms[new_character.x][new_character.y]
                    fight = False
                    return new_character.currentRoom
                else:
                    return "You can't run away from a fight!"
            else:
                return "There is nothing to run from..."  
                    
        
        if x == "pet" or x == "hug":
            Pet = False
            new_character.currentRoom.check_scharacter()
            if new_character.currentRoom.scharacters != "":
                for x in all_scharacters:
                    for y in new_character.currentRoom.scharacters:
                        if x == y:
                            Pet = True
                            scharacter = x
                        else:
                            Pet = False
                              
            if Pet == True:
                print("\n %s" %(scharacter))  
                if new_character.luck > 5:
                    powerup_gained = scharacter.power_up(new_character)
                    new_strength = new_character.change_strength(powerup_gained)
                    if "sponge" in new_character.inventory:
                        new_character.pick_up_item("key")
                        return "You gained a Gold Coin! \nThis added %d to your strength! \n\nBut this time, next to the gold coin, there is a mysterious key! \nYou also gained a key!" %(powerup_gained)
                    else:
                        return "You gained a Gold Coin! \nThis added %d to your strength!" %(powerup_gained)
                else:
                    outcome = scharacter.power_up(new_character)
                    return outcome
                    
            elif Pet == False:
                return "There is nothing to pet or hug here..."    
                    
        if x == "look":
            return new_character.currentRoom.description
                
        if x == "inv":
            return new_character.show_inventory() 
            
        if x == "points":
            return "You have %d points so far" %(new_character.points)  
            
        if x == "quit":
            #save_character()
            #save_rooms()
            print("Your progress has been saved")
            exit()
            
        else:
            return "[can't understand what you are trying to say, enter again]"                    

def start_game(new_character):
    global fight
    global play
    room = new_character.currentRoom
    intro = "--You are stuck in a house which is unfamiliar to you-- \n--Your objective is to find the exit--\n" 
    print("%s\n %s" %(intro, room))
    while play == True:
        
        new_character.currentRoom.spawn_enemy()
        enemy_present = check_enemies(new_character)
        if enemy_present == True:
            for x in all_enemies:
                if x != "":
                    enemy = x
            print("\nbut then you notice someone is watching... \noh no! An enemy has appeared! \n%s" %(enemy))
            print("\n-You have enetered a fight, what are you going to do?-")
            fight = True
            while fight == True:
                a_string = input(">")
                outcome = sentence_parsing(a_string, new_character, enemy)
                #if fight == False:
                    #print("\n", outcome)
                
            if fight == False:
                enemy_present = check_enemies(new_character)
                if enemy_present == True:
                    all_enemies.remove(enemy)
                    new_character.currentRoom.enemies.remove(enemy)
                
        
        a_string = input(">")
        fight = False
        enemy = ""
        outcome = sentence_parsing(a_string, new_character, enemy)
        print("\n", outcome)
        
            
def get_points(item, points, items):
    position = item.index(item)
    points = points[position]
    return points

def check_enemies(new_character):
    global enemy_present
    for x in new_character.currentRoom.enemies:
        if x in all_enemies:
            enemy_present = True
        else:
            enemy_present = False
        return enemy_present
            
def battle(new_character, enemy):
    global fight
    print("\n-%s's Turn-\n"%(new_character.name))
    health_lost1 = new_character.attack()
    enemy.change_health(health_lost1)
    if enemy.health > 0:
        print("\n%s lost %d health, but that wasn't enough to kill him \nThe enemy has %d health left" %(enemy.name, health_lost1, enemy.health))
    elif enemy.health <=0:
        print("\n%s has lost all of their helath! You have defeated %s!" %(enemy.name, enemy.name))
        points = new_character.change_points(50)
        print("You now have %d points by gaining 50 points" %(points))
        fight = False
        
    if enemy.health > 0:    
        print("\n-%s's Turn-\n" %(enemy.name))
        health_lost2 = enemy.attack()
        new_character.change_health(health_lost2)
        if new_character.health > 0:
            print("Thankfully, you didn't die but now you are left with %d health" %(new_character.health))
        elif new_character.health <=0:
            print("Unfortunately, you have lost all your health and died \n\n--You Lose!--")
            exit()
            
def enemy_only_attack(new_character, enemy):
    print("\n-%s's Turn-\n" %(enemy.name))
    health_lost2 = enemy.attack()
    new_character.change_health(health_lost2)
    if new_character.health > 0:
        print("Thankfully, you didn't die but now you are left with %d health" %(new_character.health))
    elif new_character.health <=0:
        print("Unfortunately, you have lost all your health and died \n\n--You Lose!--")
        exit()
    
def save_character():
    global character_list
    save_c = open("character.pickle", "wb")
    pickle.dump(character_list, save_c)
    save_c.close()
    
def load_character():
    global character_list
    load_c = open("character.pickle", "rb")
    character_list = pickle.load(load_c)
    load_c.close()
    
def save_rooms():
    global all_rooms
    save_r = open("rooms.pickle", "wb")
    pickle.dump([all_rooms], save_r)
    save_r.close()
    
def load_character_room(position):
    global all_rooms
    load_r = open("rooms.pickle", "rb")
    all_rooms_file = pickle.load(load_r)
    all_rooms = [[all_rooms_file[position]],
                 [all_rooms_file[position + 1]] ]
    
    load_r.close()

main_menu()
                        
        
    
    
    
    
    
    
    
    

