"""This module contains action functions that perform a greeting."""

import random
#import datetime
import synthesizer as synth

GREETINGS_INFORMAL = (
    "hello",
    "hi",
    "hey"
)

def informal():
    """This function replies to an informal greeting."""
    synth.speak(random.choice(GREETINGS_INFORMAL))

def formal(text):
    """This function replies to a formal greeting."""
    hour = datetime.datetime.now().hour
    time_of_day = None

    # Determine the time of day
    if hour < 12:
        time_of_day = "morning"
    elif hour < 17:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    # Add "or perhaps <time of day>" if the input doesn't match reality
    synth.speak(text + ((", or perhaps " + time_of_day)
                        if time_of_day not in text else ""))
