import os
import importlib
import time
from art import text2art

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_available_chapters():
    """Scans the 'chapters' folder inside src and returns a list of chapter names."""
    chapters_dir = os.path.join(os.path.dirname(__file__), "chapters")
    if not os.path.exists(chapters_dir):
        print("Error: The 'chapters' directory was not found.")
        return []
    
    chapter_files = [
        f[:-3] for f in os.listdir(chapters_dir)
        if f.endswith('.py') and f != '__init__.py'
    ]
    return sorted(chapter_files)

def show_menu():
    clear_screen()

    title_art = text2art("RAVI'S WORLD", font="tarty1")
    subtitle_art = text2art("Let's Drink Horror", font="small")

    print(title_art)
    print(subtitle_art)
    time.sleep(1)

    available_chapters = get_available_chapters()
    if not available_chapters:
        print("No chapters found.")
        input("\nPress ENTER to quit...")
        return
    
    print("        Select a Chapter:")
    for i, chapter_name in enumerate(available_chapters, 1):
        display_name = chapter_name.replace("chapter", "Chapter ").replace("_", " ").title()
        print(f"        {i}. {display_name}")

    print("        Q. Quit\n\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == 'q':
            input("Press Enter to quit...")
            exit()
        
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(available_chapters):
                selected_chapter_name = available_chapters[choice_index]
                chapter_module = importlib.import_module(f'chapters.{selected_chapter_name}')
                
                print(f"Starting {selected_chapter_name}...")
                clear_screen()
                chapter_module.start_game()
                break
            else:
                print("Invalid chapter number. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number or 'q'.")
        except AttributeError:
            print(f"Error: The selected chapter file '{selected_chapter_name}.py' is missing the 'start_game' function.")
            input("\nPress ENTER to return to the main menu...")
            clear_screen()
            show_menu()
