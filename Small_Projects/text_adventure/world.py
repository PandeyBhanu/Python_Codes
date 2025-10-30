from entities import Room, Item, NPC

def build_world():
    # Creating rooms 
    cave_entrance = Room("Cave Entrance", "You are standing at the entrance of a dark, damp cave.")
    dark_tunnel = Room("Dark Tunnel", "A narrow tunnel stretches into darkness.")
    treasure_room = Room("Treasure Room", "You see a room glittering with gold and jewels!")

    # Connecting rooms
    cave_entrance.add_exit("north", dark_tunnel)
    dark_tunnel.add_exit("south", cave_entrance)
    dark_tunnel.add_exit("north", treasure_room)
    treasure_room.add_exit("south", dark_tunnel)

    # Adding items 
    sword = Item("rusty sword", "An old sword. Still sharp enough to be useful.")
    key = Item("silver key", "A small key engraved with a sun symbol.", usable_on=["treasure chest"])
    cave_entrance.add_item(sword)
    dark_tunnel.add_item(key)

    # Adding NPCs 
    goblin = NPC("Goblin", "A small green creature blocks your way.", dialogue=["Grrr! This is my treasure!"], hostile=True)
    treasure_room.add_npc(goblin)

    # Starting room
    start_room = cave_entrance

    return start_room
