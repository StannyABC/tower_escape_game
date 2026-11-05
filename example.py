"""
features_demo.py
Teaching demo of two game features: rising water and miss a go.

This is not a coursework solution. It is a one-dimensional tower climb with
no maze, walls or classes, so the two rules are easy to see on their own.

Run: python3 features_demo.py
"""

TOP_FLOOR = 7
TRAP_FLOORS = {2, 5}
TURNS_PER_WATER_RISE = 2


def print_tower(state):
    """Print the tower from top to bottom, showing the player and water."""
    for floor in range(TOP_FLOOR, -1, -1):
        if floor == state["floor"]:
            square = "P"
        elif floor == TOP_FLOOR:
            square = "E"
        elif floor <= state["water_level"]:
            square = "~"
        elif floor in TRAP_FLOORS:
            square = "T"
        else:
            square = "."
        print(f"{floor}: {square}")


def take_turn(state):
    """Run the player's part of a turn. Return False if the player quits."""
    # Miss a go: use up the penalty instead of asking for a move.
    if state["miss_next_go"]:
        print("You are stuck in a trap and miss this go!")
        state["miss_next_go"] = False
        return True

    while True:
        choice = input("Climb (c), wait (w) or quit (q): ").strip().lower()
        if choice == "q":
            return False
        if choice == "w":
            return True
        if choice == "c":
            state["floor"] += 1
            # Miss a go: landing on a trap sets the penalty for the next turn.
            if state["floor"] in TRAP_FLOORS:
                print("You landed on a trap!")
                state["miss_next_go"] = True
            return True
        print("Please enter c, w or q.")


def update_water(state):
    """Count the turn and raise the water when enough turns have passed."""
    state["turns"] += 1
    if state["turns"] % TURNS_PER_WATER_RISE == 0:
        state["water_level"] += 1
        print(f"The water rises to floor {state['water_level']}!")


def main():
    """Set up the game and repeat turns until the player wins, loses or quits."""
    state = {
        "floor": 0,
        "water_level": -1,  # -1 means the water is below the bottom floor.
        "turns": 0,
        "miss_next_go": False,
    }

    print("Reach the exit (E) before the water (~) reaches you.")

    while True:
        print_tower(state)

        if not take_turn(state):
            print("Game ended.")
            return

        # Check for a win first, so reaching the exit always counts.
        if state["floor"] == TOP_FLOOR:
            print(f"You escaped in {state['turns'] + 1} turns!")
            return

        update_water(state)

        if state["floor"] <= state["water_level"]:
            print("The water caught you. You lose!")
            return


if __name__ == "__main__":
    main()