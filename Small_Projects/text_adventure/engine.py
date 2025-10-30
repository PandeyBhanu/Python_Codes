def parse_command(player, command):
    tokens = command.lower().split()
    if not tokens:
        return "Enter a command"
    
    verb = tokens[0]

    if verb in ["go" , "move"]:
        if len(tokens) > 1:
            return player.move(tokens[1])
        return "Go where?"
    
    elif verb in["take","pick", "grab"]:
        if len(tokens) > 1:
            return player.pick_item(" ".join(tokens[1:]))
        return "Take what?"
    
    elif verb == "use":
        if len(tokens) > 1:
            return player.use_item(" ".join(tokens[1:]))
        return "Use what?"

    elif verb == "inventory":
        if player.inventory:
            return "You have: " + ", ".join(i.name for i in player.inventory)
        return "Your inventory is empty."

    elif verb in ["talk", "speak"]:
        if len(tokens) > 1:
            npc_name = " ".join(tokens[1:])
            for npc in player.current_room.npcs:
                if npc.name.lower() == npc_name:
                    return npc.talk()
            return f"No one named {npc_name} here."
        return "Talk to whom?"

    elif verb in ["look", "inspect"]:
        return player.current_room.describe()

    elif verb in ["exit", "quit"]:
        return "quit"

    return "I don't understand that command."