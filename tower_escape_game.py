TOP_FLOOR = 6
TRAP_TILE = [{2,2},{1,3},{0,5},{1,5}]
ELIM_LAYER_TURNS_PER_RISE = 2

def display_tower():
    print("display tower")

def take_turn():
    print("player action")


def update_elimination_layer():
    print("layer rises or doesnt")

def main():
    # execute the objects
    print("game on or off")

    game_state = {
        "floor":0,
        "elim_layer": -1, # elim layer is below the player, will not move before 2 turns have passed
        "turns": 0,
        "miss_a_go": False
    }

main()