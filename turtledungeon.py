class Turtle:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, other_turtle):
        other_turtle.health -= self.strength
        print(f"{self.name} attacked {other_turtle.name} and did {self.strength} damage!")

import random

def start_game():
    print("Welcome to the Turtle Dungeons!")

    # Create a turtle for the player to control
    player = Turtle("Leonardo", 10, 2)

    # The dungeon is represented as a list of rooms
    # Each room is a single turtle
    dungeon = [
        Turtle("Michelangelo", 10, 2),
        Turtle("Donatello", 10, 2),
        Turtle("Raphael", 10, 2),
        Turtle("Splinter", 10, 2),
        Turtle("Shredder", 10, 3)
    ]

    # Keep track of the player's current position in the dungeon
    x = 0

    # Start the game loop
    while True:
        # Print the current room
        print(f"You are in room {x}")
        print("You see the following turtle:")
        turtle = dungeon[x]
        print(f"- {turtle.name} ({turtle.health} health)")

        # Let the player choose what to do
        action = input("What do you want to do? (move/attack/dodge) ")

        # Handle moving to a different room
        if action == "move":
            # If the turtle is still alive, the player cannot move
            if turtle.health > 0:
                print("You must defeat the turtle in this room before you can move on!")
            else:
                direction = input("Which direction do you want to move? (forward/backward) ")
                if direction == "forward" and x < len(dungeon) - 1:
                    x += 1
                elif direction == "backward" and x > 0:
                    x -= 1
                else:
                    print("You can't move in that direction!")

        # Handle attacking the turtle
        elif action == "attack":
            # There is a 20% chance that the attack will miss
            if random.random() < 0.2:
                print("Your attack missed!")
            else:
                player.attack(turtle)
                if turtle.health <= 0:
                    print(f"{turtle.name} has been defeated!")
                    dungeon.remove(turtle)
                    if not dungeon:
                        print("You have cleared the dungeon!")
                        break

            # The turtle fights back
            turtle.attack(player)
            if player.health <= 0:
                print("You have been defeated! Game over.")
                break

        # Handle dodging the turtle's attack
        elif action == "dodge":
            # The turtle's attack misses
            print("You dodged the turtle's attack!")

    print("Thanks for playing the Turtle Dungeons!")

# Start the game
start_game()
