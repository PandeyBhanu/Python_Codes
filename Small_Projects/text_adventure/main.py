from entities import Player
from world import build_world
from engine import parse_command

def main():
    print("Welcome to the Text Adventure!")
    start_room = build_world()
    player = Player("Hero", start_room)
    print(player.current_room.describe())

    while True:
        command = input("\n> ")
        result = parse_command(player, command)
        if result == "quit":
            print("Goodbye!")
            break
        print(result)

if __name__ == "__main__":
    main()
