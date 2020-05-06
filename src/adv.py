from player import Player
from room import Room
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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

room['outside'].items.append(Item("sword", "used to attack enemy's"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Jon", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print("\n")
    print(player.current_room.name)
    print(player.current_room.description)
    print("Items:")
    for item in player.current_room.items:
        print(item.name)
    direction = input("Enter a command: ").split(" ")


    if len(direction) == 2:
        if direction[0] == "get":
                for item in player.current_room.items:
                    if item.name == direction[1]:
                        player.inventory.append(item)
                        player.current_room.items.remove(item)
                        print(f'Player picked up {item.name}')
                    else:
                        print(f'There is no item named"{direction[1]}"')
                    
    elif len(direction) == 1:
        try:
            if direction[0] == 'q':
                break
            elif direction[0] == 'n':
                if player.current_room.s_to:
                    player.current_room = player.current_room.s_to
                else:
                    print("\n There is no room to the North!")
            elif direction[0] == 's':
                if player.current_room.n_to:
                    player.current_room = player.current_room.n_to
                else:
                    print("There is no room to the South!")
            elif direction[0] == 'e':
                if player.current_room.w_to:
                    player.current_room = player.current_room.w_to
                else:
                    print("There is no room to the East!")
            elif direction[0] == 'w':
                if player.current_room.e_to:
                    player.current_room = player.current_room.e_to
                else:
                    print("There is no room to the West!")
            elif direction[0] == "i":
                print(f"{player.name}'s inventory: ")
                for item in player.inventory:
                    print(item.name)
                print("\n")
        except:
            print("Enter a value")


print("Thanks for playing")
