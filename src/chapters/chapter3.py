# src/chapters/chapter3.py

import subprocess
import sys
import os
from start import pause, clear_screen


# This system is different compared to both Chapter 1 and 2 and future chapters.
def choose_option(prompt, options):
    """Display choices and return the selected option number."""
    print("\n" + prompt)

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("\nChoose an option: "))
            if 1 <= choice <= len(options):
                return choice
            print("Please choose a valid option.")
        except ValueError:
            print("Please enter a number.")


def chapter_3_start_game(game_state=None):
    """Start Chapter 3 of the game."""
    if game_state is None:
        game_state = {}

    clear_screen()
    print("\n" + "=" * 50)
    print("CHAPTER 3 - THE STICKY BANK JOB")
    print("=" * 50)

    print("\nDr. Θ has escaped Slime Prison Level 2.")
    print("He walks away from the Small C doorway.")
    pause()

    print("\nHe needs somewhere to cause more trouble.")
    print("Fortunately, he knows about Raviolo's network of")
    print("wormhole-linked facilities.")
    pause()

    print("\nDr. Θ decides to travel to Manhattan.")
    print("His route will take him through the facilities.")
    pause()

    travel_to_manhattan(game_state)


def travel_to_manhattan(game_state):
    """Travel from Sydney HQ to Manhattan through the facility network."""
    clear_screen()

    print("\nDr. Θ arrives at Sydney HQ.")
    print("One of Raviolo's wormholes is waiting.")
    pause()

    print("\nDestination: Michigan Facility")
    print("Travel method: Raviolo Wormhole")
    pause()

    print("\nDr. Θ steps into the wormhole.")
    print("The world around him twists and disappears.")
    pause()

    print("\nWHOOSH!")

    print("\nDr. Θ arrives at the Michigan Facility.")
    pause()

    print("\nOne more destination remains.")
    print("Manhattan.")
    pause()

    print("\nDr. Θ arrives in Manhattan.")
    pause()

    manhattan_arrival(game_state)


def manhattan_arrival(game_state):
    """Dr. Θ begins walking through Manhattan."""
    clear_screen()

    print("\nDr. Θ looks around Manhattan.")
    print("The streets are busy.")
    pause()

    print("\nHe starts walking down the street.")
    pause()

    print("\nUnfortunately for everyone nearby,")
    print("Dr. Θ has brought something with him.")
    pause()

    print("\nA tank filled with his special slime.")
    print("And attached to it...")
    pause()

    print("\nA minigun.")

    print("\nDr. Θ grins.")
    print('"This should be fun."')
    pause()

    # The slime gun sequence will be added here.

    print("\nDr. Θ continues walking toward his destination.")
    pause()

    # The bank section will continue from here.
    bank_arrival(game_state)


def bank_arrival(game_state):
    """Dr. Θ arrives at Manhattan City Bank."""
    clear_screen()

    print("\nDr. Θ spots a large building ahead.")
    print("\nMANHATTAN CITY BANK")
    pause()

    print("\nDr. Θ walks into the building.")
    print("He has found his target.")
    pause()

    first_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Threaten",
            "Blame"
        ]
    )

    if first_choice == 1:
        route_1(game_state)
    else:
        route_2(game_state)


def route_1(game_state):
    """First route: Threaten."""

    clear_screen()

    print("\nDr. Θ slams his hand onto the counter.")
    print('"Give me all the money!"')
    pause()

    print("\nThe bank teller, Zac, gets scared.")
    pause()

    second_choice = choose_option(
        "What does Dr. Θ do next?",
        [
            "Demand the money",
            "Show the slime gun tank"
        ]
    )

    if second_choice == 1:
        route_a1(game_state)
    else:
        route_a2(game_state)


def route_2(game_state):
    """First route: Blame."""

    clear_screen()

    print("\nDr. Θ points at Zac.")
    print('"This is all your fault!"')
    pause()

    print("\nZac asks him to leave.")
    pause()

    second_choice = choose_option(
        "What does Dr. Θ do next?",
        [
            "Insist",
            "Accuse Zac"
        ]
    )

    if second_choice == 1:
        route_c1(game_state)
    else:
        route_c2(game_state)


def route_a1(game_state):
    """A1 route."""

    clear_screen()

    print("\nDr. Θ demands that Zac hand over all the money.")
    pause()

    third_choice = choose_option(
        "How does Dr. Θ continue?",
        [
            "Stay silent",
            "Give Zac a warning"
        ]
    )

    if third_choice == 1:
        route_a1a(game_state)
    else:
        route_a1b(game_state)


def route_a2(game_state):
    """A2 route."""

    clear_screen()

    print("\nDr. Θ shows Zac the slime tank connected to the minigun.")
    pause()

    third_choice = choose_option(
        "How does Dr. Θ continue?",
        [
            "Point the gun at the counter",
            "Fire a slime shot"
        ]
    )

    if third_choice == 1:
        route_a2a(game_state)
    else:
        route_a2b(game_state)


def route_c1(game_state):
    """C1 route."""

    clear_screen()

    print("\nDr. Θ refuses to leave.")
    print('"I\'m not going anywhere!"')
    pause()

    third_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Wait quietly",
            "Step over the counter"
        ]
    )

    if third_choice == 1:
        route_c1a(game_state)
    else:
        route_c1b(game_state)


def route_c2(game_state):
    """C2 route."""

    clear_screen()

    print("\nDr. Θ accuses Zac of hiding the money.")
    pause()

    third_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Claim Zac is lying",
            "Demand the money"
        ]
    )

    if third_choice == 1:
        route_c2a(game_state)
    else:
        route_c2b(game_state)


def route_a1a(game_state):
    """A1A route."""
    clear_screen()

    print("\nDr. Θ waits silently.")
    pause()

    fourth_choice = choose_option(
        "What happens next?",
        [
            "Leave immediately",
            "Wait for Zac to hand over the money"
        ]
    )

    if fourth_choice == 1:
        ending("A1AA")
    else:
        ending("A1AB")


def route_a1b(game_state):
    """A1B route."""
    clear_screen()

    print("\nDr. Θ gives Zac a serious warning.")
    pause()

    fourth_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Leave immediately",
            "Keep pressuring Zac"
        ]
    )

    if fourth_choice == 1:
        ending("A1BA")
    else:
        ending("A1BB")


def route_a2a(game_state):
    """A2A route."""
    clear_screen()

    print("\nDr. Θ points the slime gun at the counter.")
    pause()

    fourth_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Tell Zac to hand over everything",
            "Fire the gun"
        ]
    )

    if fourth_choice == 1:
        ending("A2AA")
    else:
        ending("A2AB")


def route_a2b(game_state):
    """A2B route."""
    clear_screen()

    print("\nDr. Θ fires a glob of slime across the bank.")
    print("SPLAT!")
    pause()

    fourth_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Demand the money",
            "Fire another shot"
        ]
    )

    if fourth_choice == 1:
        ending("A2BA")
    else:
        ending("A2BB")


def route_c1a(game_state):
    """C1A route."""
    clear_screen()

    print("\nDr. Θ simply stands there.")
    pause()

    fourth_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Ask for the money",
            "Walk away"
        ]
    )

    if fourth_choice == 1:
        ending("C1AA")
    else:
        ending("C1AB")


def route_c1b(game_state):
    """C1B route."""
    clear_screen()

    print("\nDr. Θ steps over the counter.")
    pause()

    fourth_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Take the money",
            "Confront Zac"
        ]
    )

    if fourth_choice == 1:
        ending("C1BA")
    else:
        ending("C1BB")


def route_c2a(game_state):
    """C2A route."""
    clear_screen()

    print("\nDr. Θ insists that Zac is lying.")
    pause()

    fourth_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Give Zac one last chance",
            "Leave"
        ]
    )

    if fourth_choice == 1:
        ending("C2AA")
    else:
        ending("C2AB")


def route_c2b(game_state):
    """C2B route."""
    clear_screen()

    print("\nDr. Θ demands that Zac hand over the money.")
    pause()

    fourth_choice = choose_option(
        "What does Dr. Θ do?",
        [
            "Wait for the money",
            "Use the slime gun"
        ]
    )

    if fourth_choice == 1:
        ending("C2BA")
    else:
        ending("C2BB")


def ending(ending_code):
    """Display one of the 16 Chapter 3 endings."""

    clear_screen()

    endings = {
        "A1AA": (
            "BAD ENDING",
            "Dr. Θ leaves the bank without taking the money.\n"
            "His robbery has completely failed."
        ),

        "A1AB": (
            "GOOD ENDING",
            "Zac gives Dr. Θ all the money.\n"
            "Dr. Θ grabs the cash and successfully escapes."
        ),

        "A1BA": (
            "BAD ENDING",
            "Dr. Θ leaves before Zac gives him the money.\n"
            "The robbery fails."
        ),

        "A1BB": (
            "BAD ENDING",
            "Dr. Θ keeps pressuring Zac for too long.\n"
            "The situation gets out of control and the robbery fails."
        ),

        "A2AA": (
            "GOOD ENDING",
            "Zac gives Dr. Θ all the money.\n"
            "The slime gun has done its job without needing to be fired."
        ),

        "A2AB": (
            "BAD ENDING",
            "Dr. Θ fires the slime gun inside the bank.\n"
            "The resulting chaos ruins his robbery."
        ),

        "A2BA": (
            "GOOD ENDING",
            "Dr. Θ demands the money after covering the bank in slime.\n"
            "Zac gives him everything, and Dr. Θ gets away."
        ),

        "A2BB": (
            "BAD ENDING",
            "Dr. Θ fires another slime shot instead of taking the money.\n"
            "The robbery falls apart."
        ),

        "C1AA": (
            "BAD ENDING",
            "Dr. Θ asks for the money, but his earlier behaviour has "
            "already convinced Zac to refuse."
        ),

        "C1AB": (
            "BAD ENDING",
            "Dr. Θ walks away from the bank.\n"
            "His mission is a complete failure."
        ),

        "C1BA": (
            "GOOD ENDING",
            "Dr. Θ reaches the money before Zac can stop him.\n"
            "He grabs the cash and escapes the bank."
        ),

        "C1BB": (
            "BAD ENDING",
            "Dr. Θ confronts Zac instead of taking the money.\n"
            "The opportunity is lost."
        ),

        "C2AA": (
            "BAD ENDING",
            "Dr. Θ gives Zac another chance.\n"
            "Zac refuses, and the robbery fails."
        ),

        "C2AB": (
            "BAD ENDING",
            "Dr. Θ gives up and leaves the bank."
        ),

        "C2BA": (
            "BAD ENDING",
            "Dr. Θ waits too long.\n"
            "The opportunity to take the money disappears."
        ),

        "C2BB": (
            "BAD ENDING",
            "Dr. Θ uses the slime gun instead of convincing Zac.\n"
            "The bank robbery fails."
        )
    }

    title, text = endings[ending_code]

    print("\n" + "=" * 50)
    print(f"ENDING {ending_code} - {title}")
    print("=" * 50)

    print("\n" + text)
    pause()

    ending_choice = choose_option(
        "What would you like to do?",
        [
            "Try again",
            "Return to Main Menu"
        ]
    )

    if ending_choice == 1:
        chapter_3_start_game(game_state=None)
    else:
        return_to_main_menu()


# --- Return to main menu ---
def return_to_main_menu():
    """Restart start.py to return to main menu."""
    print("\nReturning to main menu...\n")

    script_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "start.py"
    )

    subprocess.run([sys.executable, script_path])
    sys.exit()


if __name__ == "__main__":
    chapter_3_start_game()