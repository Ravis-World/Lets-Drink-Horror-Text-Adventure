# Let's Drink Horror

A Python text-adventure based off the [Raviolo The Magician](https://youtube.com/playlist?list=PLRhal9PyMmPttbSB7YvDoUY3SHRxfJ2qJ&si=vixXNa_7Wv8QHQtG) Series. Step into the role of Dr. Θ, a mischievous villain intent on sabotaging Team Toadette by creating the ultimate deadly drink. Choose bizarre ingredients, mix them with care (or chaos), and discover 16 unique endings ranging from hilarious to horrifying.

## Download

### As a Standalone Program (Windows)

1. Download the latest release from the [Releases](https://github.com/Ravis-World/Lets-Drink-Horror-Text-Adventure/releases) page.
2. You're all set.

### From Source

#### Requirements

* Python 3.8+
* The [art](https://pypi.org/project/art/) library for ASCII art
* Git

#### Instructions

1. Clone the repository with Git.
    ```bash
    $ git clone https://github.com/Ravis-World/Lets-Drink-Horror-Text-Adventure.git
    $ cd Lets-Drink-Horror-Text-Adventure
    ```
2. Install dependencies
    ```
    pip install -r requirements.txt
    ```

3. Start the game
    ```
    python src/start.py
    ```

## Gameplay

* From the main menu, select a chapter to begin.
* Each chapter is a branching text adventure with multiple paths and endings.
* Make choices to mix deadly ingredients and witness unique outcomes.
* After each ending, you can try again or return to the main menu.

## Features

* ASCII-art styled title screen using the art library.
* Boot-sequence intro with fake “loading system files”.
* Fully modular chapter system — add as many chapters as you want.

## Contributing

Contributions are welcome!

Report bugs or request features via [Issues](https://github.com/Ravis-World/Lets-Drink-Horror-Text-Adventure/issues).

Submit pull requests for new chapters, bugfixes, or gameplay improvements.

## Antivirus & Standalone Executables

When building a standalone .exe using PyInstaller (or similar tools), some antivirus programs may flag the file as suspicious. This is usually a false positive caused by how PyInstaller packages Python scripts and you are safe to download.