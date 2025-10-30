class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.npcs = []
        self.exits = {} #direction -> room
    
    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def add_npc(self, npc):
        self.npcs.append(npc)

    def describe(self):
        desc = f"\n{self.name}\n{self.description}\n"
        if self.items:
            desc += "\nItems here: "+",".join(i.name for i in self.items)
        if self.npcs:
            desc += "\nItems here: " + ", ".join(n.name for n in self.npcs)
        desc += "\nExits: " + ", ".join(self.exits.keys())
        return desc
    
class Item:
    def __init__(self, name, description, usable_on =None):
        self.name = name
        self.description = description
        self.usable_on = usable_on or []

    def use(self, target=None):
        if target and target.name in self.usable_on:
            return f"You used {self.name} on {target.name}."
        return f"{self.name} can't be used that way."

class NPC: 
    def __init__(self, name, description, dialogue= None, hostile = False, health = 100):
        self.name = name
        self.description = description
        self.dialogue = dialogue or []
        self.hostile = hostile 
        self.health = health

    def talk(self):
        return self.dialogue[0] if self.dialogue else f"{self.name} has nothing to say."
    
class Player:
    def __init__(self, name, start_room):
        self.name = name
        self.current_room = start_room
        self.inventory = []
        self.health = 100

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            return f"You move {direction}.\n{self.current_room.describe()}"
        return "You can't go that way"    
        
    def pick_item(self, item_name):
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                self.inventory.append(item)
                self.current_room.items.remove(item)
                return f"You picked up {item.name}."
        return f"No {item_name} here."
    
    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item.use()
        return f"You don't have {item_name}"