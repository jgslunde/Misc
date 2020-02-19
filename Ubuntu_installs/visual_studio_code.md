# Packages

## Markdown

* markdownlint
* Markdown Preview Enhanced

## Python

* pylint (is installed when opening a python file, requires pip installation).
* Python
* Python Indent

## C++
* C/C++
* For correct linking, make sure to configure working folders in the C/C++ extension settings, found by Ctrl+Shift+P searching for it.


# Key bindings

* "acceptSelectedSuggestionOnEnter", enter -> tab

# Spell Checker
* Install the Spell Right extension in VS Code.
* Download dictionaries (.dic and .aff) from https://github.com/titoBouzout/Dictionaries
* Create and move them to the VS Code dictionaries folder:
mkdir $HOME/.config/Code/Dictionaries/
cp English\ \(American\).dic $HOME/.config/Code/Dictionaries/
cp English\ \(American\).aff $HOME/.config/Code/Dictionaries/
* Ctrl+Shift+P, search for "Spellright: Select Dictionary (Language)". Select English.
* A little icon appears in the lower right corner, where spellcheck can be turned on/off for specific files or filetypes.
* Note that you can add words to "user dictionary", which can be found at $HOME/.config/Code/User. Might be worth backing up.