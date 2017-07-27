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

import action_greeting

import recognizer as rec
import synthesizer as synth
import query

QUERIES = (
    query.Query(lambda: exit(0), False, "exit", "quit", "stop listening"),
    query.Query(action_greeting.informal, False, "hello", "hi", "hey"),
    query.Query(action_greeting.formal, True, "good morning", "good afternoon", "good evening"),
    query.Query(lambda: synth.speak("you're welcome"), False, "thank you")
)

REDUNDANT_EXPRESSIONS = (
    "please",
    "could you",
    "can you",
    "would you",
    " thank you" # only considered redundant when following another expression
)

def cleanup(text):
    """This function cleans up the input string by removing all redundant expressions."""
    cleaned = text

    # Remove all the redundant expressions
    for exp in REDUNDANT_EXPRESSIONS:
        cleaned = cleaned.replace(exp, "")

    # Count leading spaces
    spaces_lead = 0
    for char in cleaned:
        if char == " ":
            spaces_lead += 1
        else:
            break

    # Count tailing spaces
    spaces_tail = 0
    strlen = len(cleaned)
    for i in range(strlen):
        if cleaned[strlen - 1 - i] == " ":
            spaces_tail += 1
        else:
            break

    # Return the cleaned up string without leading and trailing spaces
    return cleaned[spaces_lead : -spaces_tail if spaces_tail else None]

def process(text):
    """
    This function iterates through all the queries and tries to find the one
    that matches the user input string. If none of them match the input string
    the user is informed that his input could not have been recognized.
    """
    # Clean up the input string
    cleaned = cleanup(text)

    # Iterate through the defined queries
    for que in QUERIES:
        # Stop when a match is found
        if que.process(cleaned):
            return

    # No matching query found
    synth.speak("I don't understand: " + text)

def main():
    """This is the main function of the script."""
    while True:
        # Record audio, perform speech-to-text
        text = rec.listen()
        # If the input string is not None
        if text:
            # Print the input string
            print(text)
            # Process the input string and call the assiciated function
            process(text)

if __name__ == "__main__":
    main()
