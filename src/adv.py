import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", "overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", "narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", "treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# class Item():
#     pass

# class Entity():
#     pass

# class E_Stats():
#     pass

# class I_Stats():
#     pass

# class Mob():
#     pass

# class Inventory():
#     pass


# Make a new player object that is currently in the 'outside' room.

print(room['outside'].n_to.title)

# ? player = Player("Todd The", "outside")
# ? print(player.location)

# Write a loop that:
#


def tba():
    cardinal = {"n", "e", "s", "w"}
    describe = {"describe", "description", "describe room", "room", "current room"}
    player = Player("Todd The", "outside")
    print(player)

    while True:
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        # * Waits for user input and decides what to do.

        print(room[player.location])

        cmd = input(">>> ")

        if cmd.lower() in cardinal:            
            if cmd == "n":
                try:
                    player.location = room[player.location].n_to.title
                except AttributeError:
                    print("Cannot move in that direction.")
            if cmd == "e":
                try:
                    player.location = room[player.location].e_to.title
                except AttributeError:
                    print("Cannot move in that direction.")
            if cmd == "s":
                try:
                    player.location = room[player.location].s_to.title
                except AttributeError:
                    print("Cannot move in that direction.")
            if cmd == "w":
                try:
                    player.location = room[player.location].w_to.title
                except AttributeError:
                    print("Cannot move in that direction.")
        
        if cmd in describe:
            print(room[player.location])
        
        if cmd in {"q", "Q"}:
            print("\nThanks for playing\n")
            break


        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.
tba()
