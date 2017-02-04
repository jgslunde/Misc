# Runs a text through a huffman zip-unzip.
# Input text either as a terminal argument, or when asked.
# If both are left empty, it will use Rick Astley's "Never Gonna Give You Up"

from huffman import huffman_zip, huffman_unzip
import sys


def default_text():
    # I made this a function so I could collapse it in Atom, cuz it's so long...
    return """We're no strangers to love
    You know the rules and so do I
    A full commitment's what I'm thinking of
    You wouldn't get this from any other guy

    I just want to tell you how I'm feeling
    Gotta make you understand

    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you

    We've known each other for so long
    Your heart's been aching but you're too shy to say it
    Inside we both know what's been going on
    We know the game and we're gonna play it

    And if you ask me how I'm feeling
    Don't tell me you're too blind to see

    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you

    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you

    We've known each other for so long
    Your heart's been aching but you're too shy to say it
    Inside we both know what's been going on
    We know the game and we're gonna play it

    I just want to tell you how I'm feeling
    Gotta make you understand

    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you"""

if len(sys.argv) > 1:
    if type(sys.argv[1]) == str and len(sys.argv) == 1:
        text = sys.argv[1]
    else:
        raise TypeError("Please input only one argument of string type")
        sys.exit(0)
else:
    text = raw_input("\nInput text: ")
    if len(text) == 0:
        text = default_text()


symbols_code, zipped = huffman_zip(text)
text = huffman_unzip(symbols_code, zipped)

print "\nHuffman code: %s"%zipped

print "\nSymbols/code dict: %s"%symbols_code

print "\nOutput text:\n%s"%text

print "\nThis text was compressed to %.2f bits per symbol, or %.2f percent of 8-bit ASCII size\n"%(float(len(zipped))/(len(text)),((len(zipped)*100.0/(len(text)*8.0))))
