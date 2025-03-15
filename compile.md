# Compiling

## Prerequisites
* [Python](python.org)
* [Pyinstaller](https://pypi.org/project/pyinstaller)

## Instructions
1. Clone the repo
2. Navigate to the cloned repo
3. Run the command/s listed below in your terminal

To compile the GUI version run:
`pyinstaller --onefile --icon="MLB Logo.png" --windowed App.py`

To compile the CLI version run: (Beware that this version will only give you the score for the astros)
`pyinstaller --onefile --icon="Astroslogo.ico" --windowed CLI.py`

After pyinstaller is finished navigate into the `dist` folder, where your finished file will be.