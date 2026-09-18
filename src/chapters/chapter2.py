# src/chapters/chapter2.py

import subprocess
import sys
import os
import tempfile
import webbrowser
from start import pause, clear_screen
from .chapter3 import chapter_3_start_game

def chapter_2_start_game(game_state=None):
    """Start Chapter 2 of the game."""
    if game_state is None:
        game_state = {}

    clear_screen()
    print("\n" + "=" * 50)
    print("CHAPTER 2 - SLIME PRISON")
    print("=" * 50)

    print("\nDr. Θ's plan has failed.")
    print("He has been captured and thrown into Slime Prison.")
    print("\nUnfortunately, this isn't an ordinary prison.")
    print("Dr. Θ has been placed in Slime Prison Level 2.")
    pause()
    
    print("The slime prison's speciality is making prisoners suffer")
    print("through an endless covering of cold, sticky slime.")
    pause()
    
    print("\nCold slime slowly fills Dr. Θ's boots.")
    print("His feet are covered in goo, and his movements are restricted.")
    print("His hands are bound tightly behind him.")
    print("\nDr. Θ looks around the cell.")
    print('"There has to be a way out of here..."')
    pause()

    escape_choice(game_state)


# --- Utility for input selection ---
def choose_option(prompt, options):
    """Display a numbered list of options and return the chosen string."""
    while True:
        print("\n" + prompt)

        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        choice = input("> ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]

        print("Invalid choice, try again.")


# --- Initial escape decision ---
def escape_choice(game_state):
    """Decide how Dr. Θ will attempt to escape."""
    choice = choose_option(
        "How do you escape?",
        [
            "Take off boots",
            "Use back",
            "Wait for lunch"
        ]
    )

    game_state["escape_method"] = choice

    if choice == "Take off boots":
        boot_route(game_state)

    elif choice == "Use back":
        back_route(game_state)

    elif choice == "Wait for lunch":
        lunch_route(game_state)


# --- Route 1: Take off boots ---
def boot_route(game_state):
    print("\nDr. Θ decides to take off his boots.")
    print("The cold slime has made them extremely uncomfortable.")
    print("\nHe struggles to pull them off.")
    print("SPLORP!")
    print("The boots finally come free.")
    game_state["boots_removed"] = True
    pause()

    print("\nSomething falls out of one of the boots.")
    print("CLINK!")
    pause()

    print("\nDr. Θ looks down.")
    print("A pair of wire cutters is lying on the floor.")
    print("\nUnfortunately, his hands are still bound.")
    print("The cutters are just out of reach.")
    pause()

    print("\nDr. Θ looks at his feet.")
    print("His toes are covered in cold, sticky, gooey slime.")
    print('\n"Could I... use my toes?"')
    pause()

    choice = choose_option(
        "What do you do?",
        [
            "Grab the wire cutters with your toes",
            "Put the boots back on"
        ]
    )

    if choice == "Grab the wire cutters with your toes":
        grab_cutters_with_toes(game_state)

    else:
        clear_screen()
        game_state["boots_removed"] = False
        print("\nDr. Θ puts his boots back on.")
        print("The cold slime squelches around his feet.")
        print("\nThat didn't help much.")
        print("He decides to try something else.")

        escape_choice(game_state)


def grab_cutters_with_toes(game_state):
    clear_screen()
    print("\nDr. Θ carefully moves one goo-covered foot toward the cutters.")
    print("The slime stretches between his toes.")
    print("He tries to hook the cutters with his toes.")

    print("\nThe cutters wobble...")
    print("They almost fall away!")

    choice = choose_option(
        "How do you handle the cutters?",
        [
            "Carefully grip them between your toes",
            "Kick them closer"
        ]
    )

    if choice == "Carefully grip them between your toes":
        clear_screen()
        print("\nDr. Θ carefully grips the wire cutters between his toes.")
        print("Somehow, it works!")
        print("\nHe lifts his foot and brings the cutters toward the rope.")

    else:
        clear_screen()
        print("\nDr. Θ gives the cutters a careful kick.")
        print("CLINK!")
        print("They slide across the floor...")
        print("...and land right next to him.")

        print("\nDr. Θ uses his toes to grab them.")
        print("This time, he gets a firm grip.")

    use_wire_cutters(game_state)


def use_wire_cutters(game_state):
    """Use the cutters to remove the rope."""

    game_state["rope_removed"] = True
    remove_rope(game_state)


# --- Route 2: Use back ---
def back_route(game_state):
    clear_screen()
    print("\nDr. Θ decides to use his back.")
    print("He carefully feels around behind himself.")
    print("\nSomething feels strange.")
    print("A small raised object is hidden behind him.")
    pause()

    print("\nDr. Θ presses against it.")

    print("CLICK!")

    print("\nA hidden button has been activated.")
    pause()

    game_state["hidden_button"] = True

    print("\nSomething inside the wall moves.")
    print("The mechanism releases the rope.")
    pause()

    game_state["rope_removed"] = True

    remove_rope(game_state)


# --- Route 3: Wait for lunch ---
def lunch_route(game_state):
    clear_screen()
    print("\nDr. Θ decides not to rush.")
    print("If he's in prison, lunch should eventually arrive.")
    print("\nSo he waits.")
    pause()

    print("\n...")
    print("\n......")
    print("\n.........")
    pause()

    print("\nA prison guard eventually arrives with a meal.")
    print("The tray is pushed into the cell.")

    print("\nDr. Θ looks at the meal.")
    print('"Hmm..."')
    pause()

    choice = choose_option(
        "What do you do with the meal?",
        [
            "Use the meal to escape",
            "Eat the meal"
        ]
    )

    if choice == "Use the meal to escape":
        use_meal(game_state)

    else:
        clear_screen()
        print("\nDr. Θ eats the meal.")
        print("\nIt doesn't help him escape.")
        print("In fact, it makes him even more annoyed.")
        print("He has only just started in the mashed potatoes when")
        print("something glitters.")
        pause()

        use_meal(game_state)


def use_meal(game_state):
    clear_screen()
    print("\nDr. Θ examines the meal carefully.")
    print("There is something useful hidden among the food.")

    print("\nHe uses the meal to manipulate the prison mechanism.")
    print("The mechanism clicks.")

    print("\nCLACK!")

    print("The rope loosens and falls away.")

    game_state["rope_removed"] = True

    remove_rope(game_state)


# --- All three routes converge here ---
def remove_rope(game_state):
    """ Common point reached after the rope has been removed. All three initial escape routes converge here. """
    clear_screen()
    print("The rope is gone.")
    print("\nDr. Θ rubs his wrists.")
    pause()
    after_rope_removed(game_state)

def after_rope_removed(game_state):
    """Continue the escape after all initial routes converge."""
    if not game_state.get("boots_removed", False): # if it is false
        print("Dr. Θ looks down at his boots.")
        print("\nHe decides to take them off to feel freer.")

        pause()

        print("SQUELCH!")
        print("The first boot comes off.")

        pause()

        print("SPLOOOORP!")
        print("The second boot comes off.")

        game_state["boots_removed"] = True
    else:
        print("He looks around the prison cell.")
        print("\nSomething catches his attention.")
        print("\nOne of his boots is still lying nearby.")
        pause()

    print("Dr. Θ reaches into the boot.")
    print("SQUELCH.")
    print("\nHis hands disappear into the cold, sticky slime.")
    pause()

    print("Dr. Θ feels around inside.")
    print("\nCLUNK!")
    print("He pulls out a chisel.")

    game_state["chisel"] = True
    pause()

    print("Unfortunately, his hands are now completely covered in goo.")
    print("\nDr. Θ stares at them.")
    print('\n"Again?"')
    pause()

    clean_hands(game_state)


def clean_hands(game_state):
    """Decide how Dr. Θ will clean the goo from his hands."""
    print("The slime is incredibly sticky.")
    print("Dr. Θ needs to clean his hands before the police arrive.")

    pause()

    choice = choose_option(
        "How do you clean the goo from your hands?",
        [
            "Wipe it inside your boots",
            "Use the sink"
        ]
    )

    if choice == "Wipe it inside your boots":
        wipe_goo_in_boots(game_state)
    else:
        use_sink(game_state)


def wipe_goo_in_boots(game_state):
    """Attempt to clean the goo by wiping it inside the boots."""
    clear_screen()
    print("Dr. Θ wipes the goo from his hands inside his boots.")
    print("SQUISH.")
    pause()

    print("He stops.")
    print("\nThe boots were already full of slime.")
    print("\nNow they're even messier.")

    game_state["hands_clean"] = False
    pause()

    continue_after_cleaning(game_state)


def use_sink(game_state):
    """Try to use the inconveniently placed sink."""
    clear_screen()
    print("Dr. Θ looks at the sink.")
    print("\nIt's conveniently out of reach.")
    pause()

    print("He tries to use his foot.")
    print("\nNothing happens.")
    pause()

    print("The sink doesn't accept feet.")
    print("\nIt only accepts hands.")
    pause()

    print('"Right. Hands."')
    pause()

    print("Dr. Θ figures out how to reach the sink.")
    print("He places his hands underneath the faucet.")
    pause()

    print("WHOOSH!")
    pause()

    print("The cold water washes the slime away.")
    game_state["hands_clean"] = True
    print("\nHis hands are clean again.")
    pause()

    continue_after_cleaning(game_state)


def continue_after_cleaning(game_state):
    """Continue the chapter after the hand-cleaning choices."""
    if not game_state.get("hands_clean", False): # if it is false
        level_3_ending()
        print("GAME OVER")
        pause()
        chapter_2_start_game()
    else:
        print("Dr. Θ holds onto the chisel.")
        print("\nNow he has both hands free...")
        print("and a mysterious chisel.")

        pause()

    print("There must be another way out of Slime Prison Level 2.")

    pause()

    choice = choose_option(
        "How will Dr. Θ use the chisel?",
        [
            "Break a hole in the wall",
            "Hack the prison door",
            "Wedge the bars apart"
        ]
    )

    if choice == "Break a hole in the wall":
        break_wall()
    elif choice == "Hack the prison door":
        hack_prison_door()
    else:
        wedge_bars(game_state)


def break_wall():
    """Bad ending: Dr. Θ attempts to smash through the wall."""
    clear_screen()
    print("Dr. Θ examines the wall.")
    print("\nHe raises the chisel.")
    print("THUNK!")
    pause()

    print("A tiny chip of concrete falls onto the floor.")
    print("\nDr. Θ stares at the wall.")
    print('"This is going to take a while."')
    pause()

    print("THUNK!")
    print("THUNK!")
    print("THUNK!")
    pause()

    print("Unfortunately, the wall is far too strong.")
    print("The chisel simply isn't powerful enough to make a hole.")
    pause()

    level_3_ending()


def hack_prison_door():
    """Bad ending: Dr. Θ tries to tamper with the prison door."""
    clear_screen()
    print("Dr. Θ approaches the prison door.")
    print("\nHe examines the lock.")
    print("Maybe the chisel can be used to manipulate the mechanism.")
    pause()
    
    print("He carefully inserts the chisel.")
    print("\nCLINK.")
    print("Nothing happens.")
    pause()

    print("Dr. Θ pushes harder.")
    print("\nCRACK!")
    pause()

    print("The locking mechanism makes a horrible noise.")
    print("\nA red light begins flashing.")
    print("ALARM!")
    pause()

    level_3_ending()


def wedge_bars(game_state):
    """Correct solution: use the chisel as a wedge to separate the bars."""
    clear_screen()
    print("Dr. Θ examines the bars.")
    print("He notices something.")
    print("\nOne of the bars has a tiny gap beside it.")
    print("\nIt's not much...")
    print("But it might be enough.")
    pause()

    print("Dr. Θ slides the chisel into the gap.")
    print("\nCLINK.")
    print("\nHe grips the chisel tightly.")
    print("He pushes.")
    print("The bar moves slightly.")
    pause()

    print("Dr. Θ pushes harder.")
    print("\nSQUEEEEAK.")
    print("The bars begin to separate.")
    print("\nDr. Θ smiles.")
    print('"That\'s it!"')
    pause()

    print("He wedges the chisel farther into the gap.")
    print("The opening is now just wide enough.")
    print("\nDr. Θ squeezes sideways through the bars.")
    print("He made it!")
    pause()

    game_state["escaped_cell"] = True

    print("Dr. Θ is outside his cell.")
    
    print("\nDr. Θ reaches the end of the prison corridor.")

    pause()

    print("There it is.")
    print("The Small C doorway.")
    print("The only entrance and exit to Slime Prison.")
    print("\nUnfortunately, the doorway is locked.")

    choice = choose_option(
        "How will Dr. Θ get through the Small C doorway?",
        [
            "Find the doorway release mechanism",
            "Use the chisel on the locking mechanism",
            "Force the doorway open"
        ]
    )

    if choice == "Find the doorway release mechanism":
        use_small_c_release(game_state)
    elif choice == "Use the chisel on the locking mechanism":
        chisel_small_c_door()
    else:
        force_small_c_door()


def use_small_c_release(game_state):
    """Correct solution: find the Small C doorway release."""
    clear_screen()
    print("Dr. Θ searches around the doorway.")
    print("He notices a small panel beside the door.")

    print("\nThere is a button hidden underneath a sliding cover.")
    pause()

    print("Dr. Θ opens the cover.")
    print("There is a large button.")

    print("\nIt is labelled:")
    print("SMALL C PRISON RELEASE")
    pause()

    print("Dr. Θ stares at it.")
    
    print('\n"You have got to be kidding me."')

    print("\nHe presses the button.")
    print("BEEP.")
    print("The locks disengage.")
    print("CLUNK.")
    pause()

    print("The Small C doorway slowly opens.")
    print("Dr. Θ steps through the doorway.")
    print("He has escaped Slime Prison Level 2!")

    game_state["escaped_prison"] = True

    print("And now, it's off to cause more trouble.")
    
    print("\n\nTo Be Continued...")
    pause()
    
    ending()


def chisel_small_c_door():
    """Bad ending: Dr. Θ tries to use the chisel on the doorway."""
    clear_screen()
    print("Dr. Θ takes out the chisel.")
    print("He examines the doorway's locking mechanism.")

    print("\nMaybe the chisel can force it open.")
    pause()

    print("He wedges the chisel into the mechanism.")
    print("CLINK.")
    print("Nothing happens.")
    pause()

    print("Dr. Θ pushes harder.")
    print("CRACK!")

    print("\nThe locking mechanism breaks.")
    print("A loud alarm echoes throughout the Small C.")

    print("\nRED LIGHTS FLASH.")
    print("The prison guards have been alerted.")
    pause()

    level_3_ending()


def force_small_c_door():
    """Bad ending: Dr. Θ tries to force the Small C doorway open."""
    clear_screen()
    print("Dr. Θ grabs the Small C doorway.")

    print("\nHe pulls.")
    print("Nothing happens.")
    pause()

    print("He pulls harder.")
    print("The doorway doesn't move.")

    print("\nDr. Θ tries kicking it.")
    pause()

    print("THUD!")

    print("\nThe entire prison corridor echoes.")
    print("Dr. Θ freezes.")
    print("Footsteps.")

    print("\nThe guards heard him.")
    print("The doorway remains locked.")
    pause()

    level_3_ending()

def ending():
    choice = choose_option(
        "What do you want to do next?",
        [
            "Return to Main Menu",
            "Play Chapter 3",
            "Play Again"
        ]
    )

    if choice == "Return to Main Menu":
        return_to_main_menu()
    elif choice == "Play Chapter 3":
        chapter_3_start_game(game_state=None)
    else:
        chapter_2_start_game(game_state=None)


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


def level_3_ending():
    """Create and open the Level 3 ending as a temporary HTML document."""

    ending_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Let's Drink Horror - Level 3 Ending</title>
            <style>
                body {
                    background: #111;
                    color: #eee;
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: auto;
                    padding: 50px 25px;
                    line-height: 1.7;
                }

                h1, h2 {
                    text-align: center;
                }

                .ending {
                    margin-top: 35px;
                    padding: 25px;
                    border: 1px solid #555;
                }
            </style>
        </head>
        <body>

        <h1>LET'S DRINK HORROR</h1>
        <h2>CHAPTER 2 - LEVEL 3 ENDING</h2>

        <div class="ending">

        <p>Dr. Θ failed his mission.</p>

        <p>The police arrived before he could continue his escape.</p>

        <p>He was captured and taken to Slime Prison Level 3.</p>

        <p>The guards opened the door.</p>

        <p>Beyond it was a strange anomaly filled with stinging alien goo.</p>

        <p>Dr. Θ's bare feet touched the alien goo.</p>

        <p>The substance immediately began sending painful electrical
        stings through him.</p>

        <p>He tried to escape, but the goo pulled him deeper into the anomaly.</p>

        <p>After a minute, Dr. Θ was completely swallowed by Sting Land.</p>

        <p>His body began to change.</p>

        <p>He was no longer simply a prisoner inside the anomaly.</p>

        <p>He had become part of Sting Land itself.</p>

        <p><strong>Dr. Θ had transformed into an entity of Sting Land.</strong></p>

        <h2>GAME OVER</h2>

        </div>

        </body>
        </html>
    """

    # Create the HTML file in the system's temporary directory.
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        suffix=".html",
        delete=False
    ) as file:
        file.write(ending_html)
        ending_path = file.name

    # Open the ending in the user's default browser.
    webbrowser.open("file://" + ending_path)
    
if __name__ == "__main__":
    chapter_2_start_game()