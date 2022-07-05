# doesnt do much, just enables ANSI in windows terminal, and redirectes our print statements to windows API
import colorama


# Some ANSI escape sequences for colours and effects
# These are hexidecimal unicode character
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED,'This should be red')
print('Hello')

def colour_print(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour, etc
    :param text: The text to print.
    :param effect: The colour/affect we want.
        One of constants defined at start of the module
    """
    output = "{}{}{}".format(effect,text,RESET)
    print(output)

colorama.init()

colour_print("Hello, Red", RED)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)
colorama.deinit()

# The interpeter thats being used
#C:\Users\lenovo\pyvirtualenv\python39\Scripts\


# Improve function to allow more than one ANSI sequence to be printed by using *args
def colour_print_improved(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour, etc
    :param text: The text to print.
    :param effect: The colour/affect we want.
        Zero or more of the constants defined at start of the module
    """
    effect_string = ''.join(effects)
    output = "{}{}{}".format(effect_string,text,RESET)
    print(output)

print('*'*80)
colour_print_improved("Hello, Red", RED)
colour_print_improved("Hello, Blue", BLUE)
colour_print_improved("Hello, Blue reversed", BLUE,REVERSE)
colour_print_improved("Hello, Blue reversed and underlined", BLUE,REVERSE,UNDERLINE)
colour_print_improved("Hello, Yellow", YELLOW)
colour_print_improved("Hello, Yellow, BOLD", YELLOW,BOLD)
colour_print_improved("Hello, Bold", BOLD)
colour_print_improved("Hello, Underline", UNDERLINE)
colour_print_improved("Hello, Reverse", REVERSE)
colour_print_improved("Hello, Black", BLACK)