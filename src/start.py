import os
import subprocess
import sys
import time
import main

def pause():
    """Pause the game until the player presses Enter."""
    input("\nPress Enter to continue...")
    
    clear_screen()

def clear_screen():
    """Clear the terminal screen in a cross-platform way."""
    if os.name == "nt":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"])

def set_terminal_title(title):
    """Sets the terminal/command prompt title."""
    if os.name == 'nt':  # Windows
        subprocess.run(['cmd', '/c', f'title {title}'], check=False)
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