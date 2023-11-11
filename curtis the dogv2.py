import pickle, random, time
all_rooms = []
all_enemies = []
character_list = []
all_scharacters = []
fight = False
play = True
level_menu = False                  

class character():
    def __init__(self,name,health,strength,luck,x,y):
        self.name = name
        self.health = health
        self.strength = strength
        self.luck = luck
        self.x = x
        self.y = y
        self.points = 0
        self.level = 0
        self.currentRoom = all_rooms[x][y]
        self.inventory = [" ", " ", " ", " ", " "]
        
    def attack(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2
        attack_value = total + self.get_strength()
        print("dice 1: %d \nDice 2: %d \nGiving a total of %d \nWith added strength, the total is %d" %(dice1, dice2, total, attack_value)) 
        return attack_value
        
    def get_name(self):
        return self.name
        
    def get_health(self):
        return self.health
        
    def get_strength(self):
        return self.strength
        
    def get_luck(self):
        return self.luck
        
    def get_x(self):
        return self.x
        
    def get_y(self):
        return self.y
        
    def get_currentRoom(self):
        return self.currentRoom
        
    def get_inventory(self):
        return self.inventory     
        
    def get_points(self):
        return self.points   
        
    def get_level(self):
        return self.level
        
    def set_name(self, name):
        self.name = name
        
    def set_health(self, health, change):
        if change:
            self.health += health
        else:
            self.health = health
        
    def set_strength(self, strength, change):
        if change:
            self.strength += strength
        else:
            self.strength = strength
        
    def set_luck(self, luck, change):
        if change:
            self.luck += luck
        else:
            self.luck = luck
        
    def set_x(self, x):
        self.x = x
            
    def set_y(self, y):
        self.y = y
                    
    def set_currentRoom(self, x, y):
        self.currentRoom = all_rooms[x][y]
        return self.currentRoom
        
    def set_points(self, points, change):
        if change:
            self.points += points
        else:
            self.points = points
            
    def set_level(self, level):
        self.level = level
        
    def pick_up_item(self, item):
        place = False
        for x in self.inventory:
            if x == " ":
                self.inventory[self.inventory.index(x)] = item
                place = True
                return None
        if not place:
            return "You have no room in your inventory"
            
    def remove_item(self, item):
        self.inventory.remove(item)
        
    def show_inventory(self):
        print("\nThese items are in your inventory: ")
        for x in self.inventory:
            if x != " ":
                print(x.get_name())
        return "These may be useful later..."
        
    def move(self, direction):
        if direction == "north":
            self.set_y(self.get_y() + 1)
            self.set_currentRoom(self.get_x(), self.get_y())
            return self.currentRoom.get_description()
            
        if direction == "south":
            self.set_y(self.get_y() - 1)
            self.set_currentRoom(self.get_x(), self.get_y())
            return self.currentRoom.get_description()
            
        if direction == "east":
            self.set_x(self.get_x() + 1)
            self.set_currentRoom(self.get_x(), self.get_y())
            return self.currentRoom.get_description()

        if direction == "west":
            self.set_x(self.get_x() - 1)
            self.set_currentRoom(self.get_x(), self.get_y())
            return self.currentRoom.get_description()                        
        
    def __str__(self):
        return "%s has %d health, %d luck, %d strength and is at level %d" %(self.get_name(), self.get_health(), self.get_luck(), self.get_strength(), self.get_level())
        
        
class special_character(character):
    def __init__ (self, name, description,x, y):
        character.__init__(self, name, 0, 10000, 0, x, y)
        self.description = description
        self.currentRoom = all_rooms[x][y]
        
    def get_name(self):
        return self.name
        
    def get_description(self):
        return self.description
        
    def power_up_player(self, player):
        luck = player.get_luck()
        if luck <= 5:
            return "%s happily smiled at you" %(self.get_name())
        else:
            chance = random.randint(1, self.get_strength())
            print("%s slowly opens their mouth to reveal a gold coin"%(self.get_name()))
            return chance
            
    def __str__(self):
        return self.description
        
class room():
    def __init__(self,name,items,exits,description,exit):
        self.name = name
        self.items = items
        self.exits = exits
        self.description = description
        self.exit = exit
        self.enemies = []
        self.scharacters = []
    
    def get_name(self):
        return self.name
            
    def get_items(self):
        return self.items
        
    def set_items(self, items):
        self.items = items
            
    def get_enemies(self):
        return self.enemies
        
    def set_enemies(self, enemy, remove):
        if remove:
            self.enemies.remove(enemy)
        else:
            self.enemies.append(enemy)
        
    def get_exits(self):
        return self.exits
        
    def set_exits(self, exit, remove):
        if remove:
            self.exits.remove(exit)
        else:
            self.exits.append(exit)
        
    def get_scharacters(self):
        return self.scharacters
        
    def get_description(self):
        return self.description
        
    def get_exit(self):
        return self.exit
        
    def remove_items(self, item):
        if item in self.get_items():
            self.get_items().remove(item)
            
            
    def add_item(self, items):
        self.items.append(items)
        
    def spawn_enemy(self):
        for x in range (len(all_rooms)):
            for y in range(len(all_rooms[x])):
                if all_rooms[x][y] != "":
                    if all_rooms[x][y].get_name() == self.get_name():
                        for z in all_enemies:
                            if z.get_x() == x and z.get_y() == y:
                                self.enemies.append(z)
                                
                            
                                	
    def spawn_scharacter(self):
        for x in range(len(all_rooms)):
            for y in range(len(all_rooms[x])):
                if all_rooms[x][y] != "":
                    if all_rooms[x][y].get_name() == self.get_name():
                        for z in all_scharacters:
                            if z.get_x() == x and z.get_y() == y:
                                self.scharacters.append(z)
                    
    
class Item():
    def __init__(self, name, points, desc, picked_up):
        self.name = name
        self.desc = desc
        self.points = points
        self.picked_up = picked_up
        
    def get_desc(self):
        return self.desc
        
    def get_points(self):
        return self.points
        
    def get_name(self):
        return self.name
        
    def get_picked_up(self):
        return self.picked_up
        
    def set_picked_up(self, pick):
        self.picked_up = pick
        
def create_rooms():
    global all_rooms
    
    book = Item("book", 5, "As you open this book, you expect to see some sort of information \n... \nit's completely blank...\n", False)
    torch = Item("torch", 5, "You try to turn it on \n... \nand then you realise the button has broken off...\n", False)
    can = Item("can", 10, "", False)
    box = Item("box", 0, "", False)
    wrapper = Item("wrapper", 5, "", False)
    cup = Item("cup", 5, "", False)
    
    room1 = room("A Dark Room", [book, torch], ["north"], "A Dark Room \nYou find yourself stood in a room with no light source \nLooking around more you can see a dim light to the north of you \nand on the floor are some books and what seems to be a torch", None)
    room2 = room("Hallway", [can], ["south", "east", "hidden"], "Hallway \nYou enter a much brighter scene, but there's not much around here \nThere are a few empty drink cans on the floor with a door slightly open towards the east \nthough it does look creepy...", "south")
    room3 = room("the place you shouldn't have gone into", [box], ["west", "north"], "The place you shouldn't have gone into \nAs you look around you can see a box full of various things \nand a few doors with one open towards the north", "west")
    room4 = room("Back Room", [], ["south"], "You have entered the back room \nThe room is basically empty but with a single dog sat smiling at the back", "south")
    room5 = room("Kitchen",  [wrapper, cup], ["south", "north"], "The Kitchen \nAs you look around there isn't anything useful left in here \nthere are a few dirty cups and chocolate wrappers scattered around \nbut to the north you can see an exit!", "south")
    room6 = room("Final Boss Room", [], ["south", "west"], "The Final Boss Room \nThe final exit is to the west of you but \nYou thought it was over...", "south") 

    all_rooms = [[room1, room2, room4],
                 ["", room3, room5, room6]]
                 
def create_enemies():
    global all_enemies
    enemy = character("Strong Enemy", 10, 2, 1, 1, 1)
    enemy2 = character("Poong Poong", 100000, 200, 400, 1, 3)
    
    enemy.set_level(1)
    enemy2.set_level(10000)
    
    all_enemies.append(enemy)
    all_enemies.append(enemy2)
    
def create_special_characters():
    global all_scharacters
    dog = special_character("Curtis", "Little Dog \nThis white, fluffy and cute dog looks up at you smiling, \nas you check the collar the name reads 'Curtis'", 0, 2)
    all_scharacters.append(dog)
    
def create_character():
    create_rooms()
    create_enemies()
    create_special_characters()
    name = input("Enter your name: ") .title()
    strength = random.randint(1, 20)
    luck = random.randint(1,20)
    character1 = character(name, 20, strength, luck, 0, 0)
    return character1

def main_menu():
    try:
        load_game()
    except:
        pass
        
    global character_list
    menu = "\n1.Create a new character \n2.Load/delete your previous charater \n9.quit \n: "
    mainloop = True
    while mainloop:
        choice = input(menu)
        if choice == "1":
            player = create_character()
            if player != "":
                print("\nWelcome to the game %s!" %(player.get_name()))
                print(player)
                print("You can exit and save the game at any point by typing 'quit'\nand to save the game type 'save'\n")
                character_list.append(player)
                mainloop = False
                start_game(player)
            else:
                print("unsuccessful character creation")    
            
        if choice == "2":
            loaded = False
            num = 0
            print("\n")
            if len(character_list) == 0:
                print("There is no save data")
            else:
                loaded = True
            for users in character_list:
                num += 1
                print("%d.%s" %(num, users.get_name()))
                
            if loaded:
                name = input("Enter your name: ") .title()
                for data in character_list:
                    if data.get_name() == name:
                        loaded_character = data
                        break
                    else: 
                        loaded_character = "" 
                        
                if loaded_character != "":        
                    choice2 = input("\nwould you like to \n1.continue your game \n2.delete your character \n: ")
            
                    if choice2 == "1":
                        print("\nWelcome back %s!" %(loaded_character.get_name()))
                        create_rooms()
                        create_enemies()
                        create_special_characters()
                        loaded_character_check(loaded_character)
                        mainloop = False
                        start_game(loaded_character)
                       
                    if choice2 == "2":
                        character_list.remove(loaded_character)
                        save_game()
                        print("\nYour character has been deleted\n")
                
        if choice == "9":
            mainloop = False
            
def start_game(player):
    room = player.get_currentRoom()
    intro = "--You are stuck in a house which is unfamiliar to you--\n--Your objective is to find the exit--\n\n\nUseful shortcuts include:\n'inv' ------- to check whats in your inventory \n'points' ---- to look at your exp \n'stats' ----- to check your stats \n'look' ------ to look around the room \n'go ...' ---- to move between rooms \n'pickup ...'- to pick up an item \n'drop ...' -- to drop an item \n'exits' ----- to view the exit to the room\n...and a few more you will have to figure out\n\nThe '>' symbol indicates for your input\n"
    print("%s\n %s" %(intro, room.get_description()))
    pet = check_scharacters(player)
    time.sleep(3)
    check_fight(player, pet)
    main_game(player)
    
def main_game(player):
    global fight, play, level_menu
    while play:
        pet = check_scharacters(player)
        check_fight(player, pet)
        check_level_menu(player)
                
        a_string = input(">")
        fight = False
        enemy = ""
        outcome = sentence_parsing(a_string, player, enemy, pet)
        if outcome == None:
            print("\nI don't understand what you are trying to say")
        else:
            print("\n", outcome)
            time.sleep(3)
                                               
def check_enemies(player):
    for enemy in player.get_currentRoom().get_enemies():
        if enemy in all_enemies:
            return True, enemy
    return False, None        
            
def check_scharacters(player):
    player.get_currentRoom().spawn_scharacter()
    for character in player.get_currentRoom().get_scharacters():
        if character in all_scharacters:
            return True, character
    return False, None
    
def check_fight(player, pet):
    global fight, play
    player.get_currentRoom().spawn_enemy()
    enemy_present = check_enemies(player)
    if enemy_present[0]:
        for x in all_enemies:
            if x == enemy_present[1]:
                enemy = x
        print("\nbut then you notice someone is watching... \noh no! An enemy has appeared! \n%s \n\n-You have entered a fight, what are you going to do?-" %(enemy))
        fight = True
        while fight:
            a_string = input(">")
            outcome = sentence_parsing(a_string, player, enemy, pet)
            if outcome == None:
                print("\nI don't understand what you are trying to say")
            else:
                print("\n", outcome)
                time.sleep(5)
                
        if not fight:
            enemy_present = check_enemies(player)
            if enemy_present[0]:
                all_enemies.remove(enemy)
                player.get_currentRoom().set_enemies(enemy, True)
            if not play:
                exit()
                
def check_level_menu(player):
    global level_menu
    outcome = check_level(player)
    if outcome == None:
        pass
    else:
        print("\n", outcome)
            
    if level_menu:
        enter = False
        value = player.get_level() * 5 
        while not enter:
            choice = input("Since you have leveled up,you can add %d points to any of your stats \nSo enter the number corresponding to what you want to upgrade \n1.health \n2.luck \n3.strength \n>"%(value))
                
            if choice == "1":
                player.set_health(value, True)
                print("\nYou now have %d health" %(player.get_health()))
                enter = True
                    
            if choice == "2":
                player.set_luck(value, True)
                print("\nYou now have %d luck" %(player.get_luck()))
                enter = True
                
            if choice == "3":
                player.set_strength(value, True)
                print("\nYou now have %d strength"%(player.get_strength()))
                enter = True
                    
        if enter:
            level_menu = False
            print("The points you can upgrade your stats increase as your level increases")
            time.sleep(1)
                                
def sentence_parsing(passed_string, player, enemy, pet):
    global fight, play
    string = passed_string.split()    
    
    for x in string:
        if x == "pickup":
            if not fight:
                outcome = item_procedure(player, string)
                return outcome
                
            elif fight:  
                print("As you tried to reach for the item, the enemy attacks!")
                outcome = enemy_only_attack(player, enemy)
                return outcome
                
        elif x == "drop":
            outcome = drop_item(player, string)
            return outcome
                
        elif x == "move" or x == "go":
            move = False
            if not fight:
                for y in string:
                    for exit in player.get_currentRoom().get_exits():
                        if y == exit:
                            move = True
                    
                            if y == "north":
                                if player.get_currentRoom().get_name() == "Kitchen":
                                    check = check_key(player)
                                    if check[1]:
                                        print(check[0])
                                        return player.move("north")
                                    else:
                                        return check[0]
                                else:
                                    return player.move("north")
                    
                            if y == "south":
                                return player.move("south")
                        
                            if y == "east":
                               return player.move("east")
                    
                            if y == "west":
                                if player.get_currentRoom().get_name() == "Final Boss Room":
                                    play = False
                                    return "--You Win!-- \nPoints gained: %d \nlevel achieved: %d" %(player.get_points(), player.get_level())
                                return player.move("west")
                               
                if not move:
                    return "There are no exits in that direction"   
                        
                                
            if fight:
                print("\nAs you try to get to the exit, %s stops you and attemps to attack" %(enemy.get_name()))
                outcome = enemy_only_attack(player, enemy)
                return outcome
                
        elif x == "pet" or x == "hug":
            if pet[0]:
                scharacter = pet[1]
                print("\n %s" %(scharacter))
                return pet_procedure(player, scharacter)
            if not pet[0]:
                return "There is nothing to pet or hug here..."
                
        elif x == "attack"or x == "hit":
            if fight:
                outcome = battle(player, enemy)
                return outcome
            if not fight:
                if pet[0]:
                    return "Why would you... never mind"
                else:
                    return "There is no need to fight anyone here..."
                    
        elif x == "run":
            if not fight:
                return "There is nothing to run from in here..."
            if fight:
                return run(player)
        
        elif x == "look":
            return player.get_currentRoom().get_description()
            
        elif x == "inv":
            return player.show_inventory()
            
        elif x == "points":
            return "You have %d points so far" %(player.get_points())
            
        elif x == "stats":
            return player
            
        elif x == "quit":
            if not fight:
                play = False
                return save_game()
                
            if fight:
                return "You can't quit mid-battle" 
                
        elif x == "exits":
            return "The exit to the %s" %(player.get_currentRoom().get_exit())
            
        elif x == "save":
            return save_game()
            
        elif pet[0]:
            return "You can't %s the dog" %(x)
            
        else:
            return "'%s' is an invalid command" %(x) 
            
                
def item_procedure(player, string): 
    items = player.get_currentRoom().get_items()
    item = False
    
    for selected_item in string:
        for avalible_item in items:
            if selected_item == avalible_item.get_name():
                item = True
                if avalible_item in player.get_inventory():
                    return "You already have a %s in your inventory" %(avalible_item.get_name())
                    
                if avalible_item.get_name() == "box":
                    print("\nYou tried to pick up the box, but the box is too heavy to carry \nThen you look inside and you can see:")
                    
                    headphones = Item("headphones", 20, "They look pretty new! \nbut i don't think these would be any use to you... \n", False)
                    drum_stick = Item("drum-stick", 20, "", False)
                    another_book = Item("another-book", 20, "maybe there is something inside this book- \n... \nYou are, again, dissapointed\n", False)
                    sponge = Item("sponge", 1, "...\n", False)
                    new_items = [headphones, drum_stick, another_book, sponge]

                    player.get_currentRoom().set_items(new_items)
                    
                    for x in player.get_currentRoom().get_items():
                        print(x.get_name())
                    return "These items can now be picked up"
                    
                outcome = player.pick_up_item(avalible_item)
                if outcome != None:
                    return outcome
                
                if not avalible_item.get_picked_up():
                    avalible_item.set_picked_up(True)
                    points = avalible_item.get_points()
                    player.set_points(points, True)
                    
                else:
                    return "You have picked up a %s!" %(avalible_item.get_name())
                    
                if avalible_item.get_name() == "can":
                    if player.get_currentRoom().get_name() == "Hallway":
                        player.get_currentRoom().set_exits("north", False)
                        player.get_currentRoom().set_exits("hidden", True)
                        return "You have picked up a %s! \nThis gained you %d exp \nBut as you move it out of its place, a new exit to the north appears!" %(avalible_item.get_name(), avalible_item.get_points())
                    return "%sYou have picked up a %s! \nThis gained you %d exp" %(avalible_item.get_desc(), avalible_item.get_name(), avalible_item.get_points())
            
                    
                else: 
                    return "%sYou have picked up a %s! \nThis gained you %d exp" %(avalible_item.get_desc(), avalible_item.get_name(), avalible_item.get_points())
            
    if not item:
        return "You can't pickup a %s" %(selected_item)
        
def drop_item(player, string):
    drop = False
    num = 0
    
    for word in string:
        for item in player.get_inventory():
            if item != " ":
                if word == item.get_name():
                    player.get_inventory()[player.get_inventory().index(item)] = " "
                    player.get_currentRoom().add_item(item)
                    return "You have dropped a %s \nif you want to pickup this item again, it will be in this room" %(item.get_name())
    
    print("\nThese are the items in your inventory:")
    for item in player.get_inventory():
        if item != " ":
            num += 1
            print("%d.%s" %(num, item.get_name()))
            
    while not drop:
        item = input("\nEnter the name of the item you want to drop\nor enter 9 to exit\n>") .lower()
        if item == "9":
            drop = True
            return "You didn't drop anything"
        for items in player.get_inventory():
            if item != " ":
                if item == items.get_name():
                    player.get_inventory()[player.get_inventory().index(items)] = " "
                    drop = True
                    player.get_currentRoom().add_item(items)
                    return "You have dropped a %s \nif you want to pickup this item again, it will be in this room" %(items.get_name())
        
        print("\nThis item is not in your inventory")
                    
                    
def pet_procedure(player, scharacter):
    if player.get_luck() > 5:
        powerup_gained = scharacter.power_up_player(player)
        player.set_strength(powerup_gained, True)
        for item in player.get_inventory():
            if item != " ": 
                if item.get_name() == "sponge":
                    for second_item in player.get_inventory():
                        if second_item != " ":
                            if second_item.get_name() == "key":
                                return "You gained a Gold Coin! \nThis added %d to your strength!" %(powerup_gained)
                    key = Item("key", 0, "", False)
                    outcome = player.pick_up_item(key)
                    if outcome != None:
                        return "You gained a Gold Coin! \nThis added %d to your strength! \n\n%s also wants to give you something else \nbut he realised you inventory is full..." %(powerup_gained, scharacter.get_name())
                    return "You gained a Gold Coin! \nThis added %d to your strength! \n\nBut this time, next to the gold coin, there is a mysterious key \nYou also gained a key!" %(powerup_gained)
        return "You gained a Gold Coin! \nThis added %d to your strength!" %(powerup_gained)
    else:
        outcome = scharacter.power_up_player(player)
        return outcome
        
def battle(player, enemy):
    global fight, play
    print("\n-%s's Turn-\n"%(player.get_name()))
    enemy.set_health(-(player.attack()), True)
    
    if enemy.get_health() > 0:
        print("\nbut that wasn't enough to kill him \n%s has %d health left" %(enemy.get_name(), enemy.get_health()))
        print("\n-%s's Turn-\n" %(enemy.get_name()))
        player.set_health(-(enemy.attack()), True)
        
        if player.get_health() > 0:
            return "Thankfully, you didn't die but now you are left with %d health" %(player.get_health())
        if player.get_health() <= 0:
            fight = False
            play = False
            return "Unfortunately, you have lost all your health and died \n\n--You Lose!--\nPoints gained: %d\nLevel achieved: %d" %(player.get_points(), player.get_level())
            
            
    if enemy.get_health() <= 0:
        player.set_points(50, True)
        fight = False
        return "%s has lost all of their health! You have defeated %s! \nThis gained you 50 exp!"%(enemy.get_name(), enemy.get_name())
        
def enemy_only_attack(player, enemy):
    print("\n-%s's Turn-\n" %(enemy.get_name()))
    player.set_health(-(enemy.attack()), True)
        
    if player.get_health() > 0:
        return "Thankfully, you didn't die but now you are left with %d health" %(player.get_health())
    if player.get_health() <= 0:
        fight = False
        play = False
        return "Unfortunately, you have lost all your health and died \n\n--You Lose!--\nPoints gained: %d\nLevel achieved: %d" %(player.get_points(), plsyer.get_level())
                                              
def check_key(player):
    global play
    for item in player.get_inventory():
        if item.get_name() == "key":
            return "\nYou carefully take out he key that the cute dog gave you, \nyou then try to insert it into the lock \n... \n... \nIt works!", True #\n\n--You Win!-- \nPoints gained: %d" %(player.get_points())
    return "as you try to open the door, you realise that a key is needed", False

def check_level(player):
    global level_menu
    level =  player.get_points() // 10
    if player.get_level() != level:
        level_menu = True
        player.set_level(level)
        return "--You have leveled up! You are now level %d--\n" %(player.get_level())

def run(player):
    global fight
    if player.get_luck() <= 15:
        print("As you try to reach for the exit...\n")
        return enemy_only_attack(player, enemy)
    else:
        fight = False
        print("You have successfully run away")
        return player.move(player.get_currentRoom().get_exit())
        
        
def save_game():
    save = open("save_data.pickle", "wb")
    pickle.dump(character_list, save)
    save.close()
    return "--Your game has been saved--"
    
def load_game():
    global character_list
    load = open("save_data.pickle", "rb")
    character_list = pickle.load(load)
    load.close()
  
def loaded_character_check(player):
    global all_rooms
    for item in player.get_inventory():
        if item != " ":
            if item.get_name() == "can":
                for List in all_rooms:
                    for rooms in List:
                        try:
                            if rooms.get_name() == "Hallway":
                                rooms.set_exits("hidden", True)
                                rooms.set_exits("north", False)
                        except: #strings 
                            pass
                            
    print("\n\\\\Remember that enemies re-spawn when loading back into the game//\n")
                        
                    
main_menu()                           



