"""
This module contains the definition of the Expression class.
"""

class Expression:
    """
    An expression consists of a list of synonymous strings
    and a callback function that is called when the input
    string is matches one of the synonyms.
    """
    action = None
    matches = None

    def __init__(self, callback, *args):
        self.action = callback
        self.matches = args

    def compare(self, expr):
        """
        This method compares the input string against the
        list of synonymous expressions. Returns True if
        the list constains the input expression, False otherwise.
        """
        return expr in self.matches
