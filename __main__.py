"""
This is the main module of the Assistant project.

It is also the only module that is supposed to be executed,
all the others are only meant to be used as imports.

Inside of an infinite loop the program listens to whatever
the user says. Then it uses Google's Speech API to covert
the speech to text. Unless the conversion returned None the
input is printed to terminal and processed via the respective
function which compares it against the list of expressions.
If any of the expressions happens to be a match the callback
function of that expressions is called and the input is considered
to be successfully resolved. Otherwise the user is notified that
the program was unable to resolve the last input.
"""

import recognizer
import synthesizer
import expression

def plhldr():
    """This is a placeholder callback function"""
    synthesizer.speak("Expression recognized")

EXPRESSIONS = [expression.Expression(plhldr, "hello", "hi", "good morning")]

def process(text):
    """Function for processing the user input"""
    # Test the input string against the list of defined expressions
    for exp in EXPRESSIONS:
        # If the string matches the expression
        if exp.compare(text):
            # Call the function associated with the expression
            exp.action()

while True:
    # Record audio, perform speech-to-text
    TEXT = recognizer.listen()
    # If the input string is not None
    if TEXT:
        # Print the input string
        print(TEXT)
        # Process the input string and call the assiciated function
        process(TEXT)
