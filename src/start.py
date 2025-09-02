# This script requires the 'art' library. Install it with:
# pip install art

import os
import time
import main
from art import text2art

def clear_screen():
    """Clears the terminal screen for a cleaner display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_intro():
    """
    Displays the boot sequence for the game.
    """
    clear_screen()
    
    # Boot sequence
    boot_sequence = [
        {"text": "C:\\>", "delay": 2},
        {"text": "Loading system files...", "delay": 1},
        {"text": "DONE.", "delay": 1.5}
    ]
    
    for step in boot_sequence:
        print(step['text'])
        time.sleep(step['delay'])

    clear_screen()

def main_launcher():
    """
    The main launcher function.
    This will run the intro and then call the main menu.
    """
    show_intro()
    # Call the main menu logic from the main.py file
    main.show_menu()

if __name__ == "__main__":
    main_launcher()
