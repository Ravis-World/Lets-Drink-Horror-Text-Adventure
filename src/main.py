import os
# import chapter
from art import text2art

def clear_screen():
    """Clears the terminal screen for a cleaner display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """
    Displays the game's title screen and main menu.
    """
    clear_screen()
    
    # Use the 'art' library to generate and print the title
    title_art = text2art("Adventure", font="tarty1")
    subtitle_art = text2art("Terminal", font="small")
    
    print(title_art)
    print(subtitle_art)
    
    print("\n\n")
    print("        1. Select Chapter")
    print("        2. Quit")
    print("\n\n")

    while True:
        choice = input("> ").strip()
        if choice == '1':
            print("Starting game...")
            clear_screen()
            chapter.start_game()
            break
        elif choice == '2':
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice. Please enter '1' or '2'.")

def main():
    """The main function to call the menu sequence."""
    show_menu()

if __name__ == "__main__":
    main()
