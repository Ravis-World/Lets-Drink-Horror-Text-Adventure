# src/chapters/chapter1.py

import subprocess
import sys
import os

def start_game(game_state=None):
    """Start Chapter 1 of the game."""
    if game_state is None:
        game_state = {}

    print("\nYou are Dr. Θ. You have just devised a plan to sabotage Team Toadette.")
    print("Disguise yourself as a verified bartender and help create the ultimate death drink.\n")

    # Choose base liquid
    base = choose_option("Choose the base liquid:", ["Water", "Milk"])
    game_state['base'] = base

    if base == "Water":
        additive1_water(game_state)
    else:
        additive1_milk(game_state)


# --- Utility for input selection ---
def choose_option(prompt, options):
    """Display a numbered list of options and return the chosen string."""
    while True:
        print(prompt)
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        choice = input("> ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print("Invalid choice, try again.\n")


# --- Water branch ---
def additive1_water(game_state):
    print("\nLet's see... what goes with water?\n")
    choice = choose_option("Choose your first additive:", ["Honey", "Salt"])
    game_state['branch1'] = choice

    if choice == "Honey":
        additive2_a1(game_state)
    else:
        additive2_a2(game_state)


def additive2_a1(game_state):
    print("\nTime to kick it up a notch.\n")
    choice = choose_option("Choose your second additive:", ["Lemon Juice", "Mint Candy"])
    game_state['branch2'] = choice

    if choice == "Lemon Juice":
        final_a1a(game_state)
    else:
        final_a1b(game_state)


def additive2_a2(game_state):
    print("\nSalt... interesting choice. What next?\n")
    choice = choose_option("Choose your second additive:", ["Vinegar", "Soy Sauce"])
    game_state['branch2'] = choice

    if choice == "Vinegar":
        final_a2a(game_state)
    else:
        final_a2b(game_state)


# --- Milk branch ---
def additive1_milk(game_state):
    print("\nMilk... classic. Now, what sweet chaos can I stir in?\n")
    choice = choose_option("Choose your first additive:", ["Sugar", "Pepper"])
    game_state['branch1'] = choice

    if choice == "Sugar":
        additive2_c1(game_state)
    else:
        additive2_c2(game_state)


def additive2_c1(game_state):
    print("\nSweet, sweet poison. What's the next layer?\n")
    choice = choose_option("Choose your second additive:", ["Chocolate Syrup", "Strawberry"])
    game_state['branch2'] = choice

    if choice == "Chocolate Syrup":
        final_c1a(game_state)
    else:
        final_c1b(game_state)


def additive2_c2(game_state):
    print("\nSpicy! Let's make it even more... unique.\n")
    choice = choose_option("Choose your second additive:", ["Cinnamon", "Grated Cheese"])
    game_state['branch2'] = choice

    if choice == "Cinnamon":
        final_c2a(game_state)
    else:
        final_c2b(game_state)


# --- Final additive choices ---
def final_a1a(game_state):
    choice = choose_option("Choose the final additive:", ["Eye Drops", "Dish Soap"])
    game_state['branch3'] = choice
    opening_ritual(game_state)


def final_a1b(game_state):
    choice = choose_option("Choose the final additive:", ["Crushed Pills", "Bar of Soap"])
    game_state['branch3'] = choice
    opening_ritual(game_state)


def final_a2a(game_state):
    choice = choose_option("Choose the final additive:", ["Bleach", "Chilli Sauce"])
    game_state['branch3'] = choice
    opening_ritual(game_state)


def final_a2b(game_state):
    choice = choose_option("Choose the final additive:", ["Ink", "Toothpaste"])
    game_state['branch3'] = choice
    opening_ritual(game_state)


def final_c1a(game_state):
    choice = choose_option("Choose the final additive:", ["Glue", "Nail Remover"])
    game_state['branch3'] = choice
    opening_ritual(game_state)


def final_c1b(game_state):
    choice = choose_option("Choose the final additive:", ["Cough Syrup", "Crayon Shavings"])
    game_state['branch3'] = choice
    opening_ritual(game_state)


def final_c2a(game_state):
    choice = choose_option("Choose the final additive:", ["Shampoo", "Rusty Nail"])
    game_state['branch3'] = choice
    opening_ritual(game_state)


def final_c2b(game_state):
    choice = choose_option("Choose the final additive:", ["Slime", "Glue Stick Bits"])
    game_state['branch3'] = choice
    opening_ritual(game_state)


# --- Opening ritual / endings ---
def opening_ritual(game_state):
    print("\nHere you go... your special drink.")
    print("The guest hesitantly takes the glass.")
    print("They sip slowly...\n")

    # --- Map choices to ending key ---
    base_map = {
        "Water": "a",
        "Milk": "c"
    }
    
    branch1_map = {
        "Honey": "1",
        "Salt": "2",
        "Sugar": "1",
        "Pepper": "2"
    }

    branch2_map = {
        "Lemon Juice": "a",
        "Mint Candy": "b",
        "Vinegar": "a",
        "Soy Sauce": "b",
        "Chocolate Syrup": "a",
        "Strawberry": "b",
        "Cinnamon": "a",
        "Grated Cheese": "b"
    }

    branch3_map = {
        "Eye Drops": "a",
        "Dish Soap": "b",
        "Crushed Pills": "a",
        "Bar of Soap": "b",
        "Bleach": "a",
        "Chilli Sauce": "b",
        "Ink": "a",
        "Toothpaste": "b",
        "Glue": "a",
        "Nail Remover": "b",
        "Cough Syrup": "a",
        "Crayon Shavings": "b",
        "Shampoo": "a",
        "Rusty Nail": "b",
        "Slime": "a",
        "Glue Stick Bits": "b"
    }

    ending_key = (
        base_map[game_state['base']] +
        branch1_map[game_state['branch1']] +
        branch2_map[game_state['branch2']] +
        branch3_map[game_state['branch3']]
    )

    # --- Endings dictionary ---
    endings = {
        'a1aa': "The plush bird takes a sip... They freeze mid-sip and slowly slump over.",
        'a1ab': "The plush bird drinks... Foam bubbles from their beak, slides off the bar!",
        'a1ba': "A quick gulp... Their eyes spiral, a quiet twitch... then a backward fall.",
        'a1bb': "Another sip of soap... Spinning, gurgling foam, a stiff collapse.",
        'a2aa': "Down it goes... Locked in place, a 'statue death'!",
        'a2ab': "A spicy end! Screams erupt, steam billows... they explode in feathers!",
        'a2ba': "Dark liquid consumed... They turn black, ooze from the eyes, and fall lifelessly.",
        'a2bb': "Minty fresh... and deadly! Comedic bubble foam, squeaks, and freezes.",
        'c1aa': "A sticky situation... Mouth sealed, the bird flops stiff.",
        'c1ab': "A chemical cocktail... A dizzy collapse, chemical vapour rises!",
        'c1ba': "Sweet dreams, little bird. Dozes off peacefully, a dramatic stillness.",
        'c1bb': "A colourful end. Rainbow vomit, bird stiffens smiling.",
        'c2aa': "Lather, rinse, perish. Bubbles from the nose, plush floats away!",
        'c2ab': "Shocking! Sparks fly, plush jerks violently.",
        'c2ba': "A gooey demise. Bird melts, only a puddle remains.",
        'c2bb': "Brittleness at its finest. Cracks apart like brittle plastic."
    }

    print("\n" + endings.get(ending_key, "The ending is mysterious... You disappear in the shadows."))

    # --- Menu to try again or return to main menu ---
    choice = choose_option("\nWhat do you want to do next?", ["Try another combination", "Return to Main Menu"])
    if choice == "Try another combination":
        start_game(game_state)
    else:
        return_to_main_menu()


def return_to_main_menu():
    """Restart start.py to return to main menu."""
    print("Returning to main menu...\n")
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "start.py")
    subprocess.run([sys.executable, script_path])
    sys.exit()