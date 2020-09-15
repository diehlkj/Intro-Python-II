import sys
from room import Room
from player import Player
from items import Item, Weapon

# Declare Items 

item = {
    "torch": Item("Torch", "Gives off a small ammount of light", 5, "utility"),
    "dagger": Weapon("Dagger", "A crude dagger made of bronze. Its seen better days.", 15, "weapon", 5),
    "test_item_1": Item("Item 1", "Just a test item", 1, "test item"),
    "test_item_2": Item("Item 2", "Just a test item", 1, "test item"),
    "test_item_3": Item("Item 3", "Just a test item", 1, "test item"),
    "test_item_4": Item("Item 4", "Just a test item", 1, "test item"),
    "test_item_5": Item("Item 5", "Just a test item", 1, "test item"),
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "outside",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", "foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["test_item_2"]]),

    'overlook': Room("Grand Overlook", "overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item["test_item_3"]]),

    'narrow':   Room("Narrow Passage", "narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item["test_item_4"]]),

    'treasure': Room("Treasure Chamber", "treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item["test_item_5"]]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#





def tba():
    cardinal = {"n", "e", "s", "w", "north", "south", "east", "west"}
    end = {"quit", "q", "end", "exit", "stop", "close"}
    inventory = {"inventory", "items", "bag", "inv"}
    
    player = Player("Todd The", room["outside"], [item["torch"], item["dagger"]])
    # print(player)
    
    print(player.location)
    
    while True:
        cmd = input("\n>>> ")
        cmdSplit = cmd.split()
        
        if len(cmdSplit) > 1:
            if cmdSplit[0].lower() == "get":
                player.getItem(cmdSplit[1].lower())
            
            if cmdSplit[0].lower() == "drop":
                player.dropItem(cmdSplit[1].lower())
                
            if cmdSplit[0].lower() == "describe":
                pass
        else:
            # ? Movement
            if cmd.lower() in cardinal:
                if cmd == "n":
                    try:
                        player.location = room[player.location.title].n_to
                        print(player.location)
                    except AttributeError:
                        print("\nCannot move in that direction.")
                if cmd == "e":
                    try:
                        player.location = room[player.location.title].e_to
                        print(player.location)
                    except AttributeError:
                        print("\nCannot move in that direction.")
                if cmd == "s":
                    try:
                        player.location = room[player.location.title].s_to
                        print(player.location)
                    except AttributeError:
                        print("\nCannot move in that direction.")
                if cmd == "w":
                    try:
                        player.location = room[player.location.title].w_to
                        print(player.location)
                    except AttributeError:
                        print("\nCannot move in that direction.")
            
            elif cmd.lower() in inventory:
                print("\n")
                for count, i in enumerate(player.inventory):
                    print(f"{count}: {i.name}")
            
            elif cmd.lower() in end:
                print("\nThanks for playing\n")
                break
            
            else:
                print(f"\nUnknown command: {cmd}")


        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
tba()
