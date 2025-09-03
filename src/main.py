import os
import importlib
from art import text2art

def clear_screen():
    """Clears the terminal screen for a cleaner display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_available_chapters():
    """Scans the 'chapters' folder and returns a list of chapter names."""
    chapters_dir = "chapters"
    if not os.path.exists(chapters_dir):
        print("Error: The 'chapters' directory was not found.")
        return []
    
    # List all .py files and remove the extension and __init__.py
    chapter_files = [
        f[:-3] for f in os.listdir(chapters_dir) 
        if f.endswith('.py') and f != '__init__.py'
    ]
    
    # Sort the list alphabetically for consistent menu order
    return sorted(chapter_files)

def show_menu():
    """
    Displays the game's title screen and main menu with dynamic chapters.
    """
    clear_screen()
    
    # Use the 'art' library to generate and print the title
    title_art = text2art("RAVIS WORLD", font="tarty1")
    subtitle_art = text2art("Let's Drink Horror", font="small")
    
    print(title_art)
    print(subtitle_art)
    
    print("\n\n")
    
    available_chapters = get_available_chapters()
    if not available_chapters:
        print("No chapters found.")
        print("Please add .py files to the 'chapters' folder.")
        input("\nPress ENTER to quit...")
        return
        
    print("        Select a Chapter:")
    for i, chapter_name in enumerate(available_chapters, 1):
        # Format the chapter name for the menu (e.g., "chapter1" -> "Chapter 1")
        display_name = chapter_name.replace("chapter", "Chapter ").replace("_", " ").title()
        print(f"        {i}. {display_name}")

    print("        Q. Quit")
    print("\n\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == 'q':
            input("Press Enter to quit...")
            exit()
        
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(available_chapters):
                selected_chapter_name = available_chapters[choice_index]
                # Dynamically import the selected chapter module
                chapter_module = importlib.import_module(f'src.chapters.{selected_chapter_name}')
                
                print(f"Starting {selected_chapter_name}...")
                clear_screen()
                # Run the game from the selected chapter
                chapter_module.start_game()
                break # Exit the menu loop after the game returns
            else:
                print("Invalid chapter number. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number or 'q'.")
        except AttributeError:
            print(f"Error: The selected chapter file '{selected_chapter_name}.py' is missing the 'start_game' function.")
            input("\nPress ENTER to return to the main menu...")
            clear_screen()
            show_menu() # Return to the main menu on error
