import os
import time
import main
from art import text2art

def clear_screen():
    """Clears the terminal screen for a cleaner display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def set_terminal_title(title):
    """Sets the terminal/command prompt title."""
    if os.name == 'nt':  # Windows
        os.system(f"title {title}")
    else:  # macOS/Linux
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

def show_intro():
    """Displays the boot sequence for the game."""
    clear_screen()
    set_terminal_title("Let's Drink Horror")  # <-- set the window title here
    
    boot_sequence = [
        {"text": "Copyleft Ravi's World", "delay": 0.1},
        {"text": "C:\\>", "delay": 2},
        {"text": "Loading system files...", "delay": 1},
        {"text": "DONE.", "delay": 1.5}
    ]
    
    for step in boot_sequence:
        print(step['text'])
        time.sleep(step['delay'])

    clear_screen()

def main_launcher():
    """The main launcher function."""
    show_intro()
    main.show_menu()

if __name__ == "__main__":
    main_launcher()