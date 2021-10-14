# I wanted to learn more Python class structures. What better way to do that than creating a dungeon crawler in 32 lines or less.
# How to play. The first level you will die if you don't heal yourself, so make sure you do that. Once level two you can hold down Enter til you get to level 10 and beat the game.
# There are lots of opportunities to take this code and make add RNG, loot, this or that. Maybe one day I'll come back to that but not today. 

import random, os
playing = True

# Where all game data is stored. If you want to add, edit or subtract anything, use a json beautifier to make it bigger. Right now it's minified to reduce line count.
levels = {1: 100, 2: 200, 3: 400, 4: 800, 5: 1600, 6: 3200, 7: 6400, 8: 12800, 9: 25600, 10: 512000}
titles = {"Ferocious":{"name":"Ferocious"},"Angry":{"name":"Angry"},"Mean":{"name":"Mean"},"Strong":{"name":"Strong"},"Simple":{"name":"Simple"}}
monster_list = {"Goblin":{"name":"Goblin","hp":40,"atk":7},"Orc":{"name":"Orc","hp":50,"atk":10},"Bat":{"name":"Bat","hp":25,"atk":10},"Rat":{"name":"Goblin","hp":10,"atk":5},"Vampire":{"name":"Vampire","hp":100,"atk":5},"Wolf":{"name":"Wolf","hp":80,"atk":10},"Mind Flayer":{"name":"Mind Flayer","hp":30,"atk":10},"Werewolf":{"name":"Werewolf","hp":80,"atk":10}}
room_list = {"1":{"name":"Dining hall","description":"It's a beautiful, expansive hall. Before you is a long table surrounded by chairs. At the very end of the chair is a skeleton with a head on it.","action":"inspect the skeleton","action_description":"You touch the skeleton and it suddenly collapses into dust. You hear a screech coming from above and before you lands a monster."},"2":{"name":"Hallway","description":"It's a hallway. It has paintings along the way and a few doors you can check out.","action":"inspect the painting","action_description":"You investigate one of the paintings. Its a hill with a cottage sitting on it and a tree. You notice something in the tree and as you get closer to check, you hear something down the hall."},"3":{"name":"Kitchen","description":"It's a kitchen. There are many things in the kitchen but you seem to notice a ham on the counter.","action":"eat the ham","action_description":"After eating the ham, you suddenly realize all your life choices have led to this moment. You hear a screech coming from the refrigerator."},"4":{"name":"Bedroom","description":"It's a small bedroom with the standard fare of bedroom things. A dresser, a bed and a window.","action":"look out the window","action_description":"You look out the window. You wonder how long you've been in this place and wonder if you'll ever get out. You suddenly hear a roar behind you."},"5":{"name":"Secret corridor","description":"It's a secret corridor. Interesting. You're not sure how you got in here, but you know you must follow the torch lights to get out.","action":"grab a torch","action_description":"You grab a torch. You use this for awhile to walk down but the torch light begins to fade. As the last light fades, so does the hope you feel and you begin to hear a scream behind you."},"6":{"name":"Workshop","description":"It's a workshop of some kind. Many interesting things hang along the wall but one in particular catches your eye.","action":"inspect the craft","action_description":"You investigate the craft. It's unlike anything you've ever seen. It resembles a blue C but with two green waves going through it. While you wonder what this could mean, a yell can be heard from the next room."},"7":{"name":"Bathroom","description":"It's a bathroom. It's not that interesting. The shower curtain is closed.","action":"open the shower curtain","action_description":"You open the shower curtain and what should appear?"},"8":{"name":"Attic","description":"It's the attic. You're not sure how you got here, but you did. There's a box sitting alone by itself.","action":"open the box","action_description":"You open the box. The box is empty. This is disappointing because the author didn't create an Loot class for you to get loot. Yeah, yeah, you hear a roar behind you."},"9":{"name":"Courtyard","description":"It's a courtyard. It's interesting to wonder how you wound up here, but now you are here. There's a water fountain in the couryard.","action":"check out the water fountain","action_description":"You walk over to the water fountain and inspect it. It looks like an ordinary water fountain. You look down and find a note. You pick it up and read it. It says 'Healthcare is too important to stay the same'. You're not sure why this was left here. You drop the note after hearing a scream behind you."}}

# Define our classes and init attributes
# These classes could be expanded more. For example, level up code should exist within the Player object. If the monsters attack/heal or rooms "speak" or are manipulated, that code should exist in the class. 

class Monster:
    def __init__(self, name, hp, atk):
        self.name = name; self.hp = hp; self.atk = atk

class Room:
    def __init__(self, name, description, action, action_description):
        self.name = name; self.description = description; self.action = action; self.action_description = action_description

class Player:
    def __init__(self, name, hp, atk, lvl, heal, xp, monster_kills, rooms_entered):
        self.name = name; self.hp = hp; self.atk = atk; self.lvl = lvl; self.heal = heal; self.xp = xp; self.monster_kills = monster_kills; self.rooms_entered = rooms_entered

# Clear the screen once in awhile. We'll be calling this a lot.
def clear():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

# Header to print at top of game screen. This is always first function to be called after clear()
def get_header(name, lvl, xp, hp):
    xp_to_next_level = levels[player.lvl]
    stats = f"{name} - Lvl {lvl} - XP: {xp}/{xp_to_next_level} - HP: {hp}"
    game_title = "Console Quest"
    header = game_title + "\n" + stats
    return header

# Battle loop. This could be a Class object but it's not really required since we won't be reusing this often, just called as part of a loop. 
def battle(player, monster):

    # gather monster.hp and player.hp as new variables so we don't modify the class object. 
    monster_hp = monster.hp
    player_hp = player.hp
    monster_stats = f"{monster.name} - HP: {monster_hp}"
    player_stats = get_header(player.name, player.lvl, player.xp, player.hp)
    print(f"{player_stats}")
    input(f"A {monster.name} appears.\n")
    clear()

    # while monster is alive, keep fighting.
    while(monster_hp >= 1):
        monster_stats = f"{monster.name} - HP: {monster_hp}"
        player_stats = get_header(player.name, player.lvl, player.xp, player_hp)
        print(f"{player_stats} | {monster_stats}\n")
        input(f"{monster.name} attacks {player.name} for {monster.atk} points.")
        clear()
        player_hp = player_hp - monster.atk
        player_stats = get_header(player.name, player.lvl, player.xp, player_hp)
        print(f"{player_stats} | {monster_stats}\n")

        if (player_hp <= 0):
            print(f"{player.name} has been slain. You got to level {player.lvl} and killed {player.monster_kills} monsters.")
            quit()
        player_actions = input("[Enter] Attack, [1] Heal, [2] Run away\n")

        if (player_actions == ""):
            input(f"{player.name} has attacked {monster.name} for {player.atk} points.")
            monster_hp = monster_hp - player.atk
            clear()
        elif(player_actions == "1"):
            input(f"{player.name} has healed for {player.heal} points.")
            player_hp = player_hp + player.heal
        if(player_hp > player.hp):
            player_hp = player.hp; clear()
        elif(player_actions == "2"):
            input(f"{player.name} has ran away.")
            break
    # When monster finally dies, calculate XP
    if (monster_hp <= 0):
        xp_gained = player.lvl * monster.hp
        player.xp = player.xp + xp_gained
        player.monster_kills = player.monster_kills + 1
        player_stats = get_header(player.name, player.lvl, player.xp, player_hp)
        print(f"{player_stats}")
        input(f"{player.name} earned {xp_gained} experience points from slaying {monster.name}")
    
    # Level up code. 
    if(player.xp >= levels[player.lvl]):
        # stat increases
        player.lvl = player.lvl + 1
        player.hp = player.hp * 2
        player.atk = player.atk * 2
        player.heal = player.heal * 2
        input(f"Ding! {player.name} leveled up to level {player.lvl}")
        # reset XP to 0 so we can start again.
        player.xp = 0


# Start the game.
print("Welcome to Console Quest, the RPG in a console. Can you survive the monotony?")
print("How to play: Just keep pressing enter. Heal yourself with the '1' key or run away with '2'.")
print("If your HP goes to 0, the game ends. This is a hardcore game, after all.")
player_name = input("Enter your character's name\n")

# Create our player object
player = Player(player_name, 50, 5, 1, 25, 0, 0, 0)
input(f"Hello {player.name}. You are level {player.lvl}. Good luck on your journey.")
clear()

# Game Loop
while (playing is True):

    # Create a room by selecting a random one from our room_list.

    room_attributes = random.choice(list(room_list.values()))
    room = Room(room_attributes['name'], room_attributes['description'], room_attributes['action'], room_attributes['action_description'])
    
    # Display room
    player_stats = get_header(player.name, player.lvl, player.xp, player.hp)
    print(f"{player_stats}\n")
    print(f"You have entered {room.name}.\n{room.description}")
    inspect_room = input(f"{room.action}")
    input(f"{room.action_description}");player.rooms_entered = player.rooms_entered + 1
    clear()
    
    # Generate monster randomly from monster_list
    monster_attributes = random.choice(list(monster_list.values()))
    monster_name = random.choice(list(titles.values()))["name"] + " " + monster_attributes["name"]
    monster = Monster(monster_name, monster_attributes['hp'], monster_attributes['atk'])

    # Enter battle
    battle(player, monster)
    
    # Cleanup room and monster objects as we'll reuse them in this loop.
    del monster, room
    clear()
    
    # If player reaches the last level in the levels list, end the game and print some stats
    if (player.lvl == list(levels)[-1]):
        input(f"Congratulations {player.name}, you beat this really simple game. You killed {player.monster_kills} monsters and went through {player.rooms_entered} rooms to get here.")
        exit()