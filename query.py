"""This module contains the definition of the Query class."""

class Query:
    """
    A query consists of a list of synonymous string expressions
    and an action function that is called when the input
    string matches one of the synonyms.
    """

    # Reference to a function that is called when the input
    # string matches one of the expressions in the list.
    action = None
    # Determines if the input string is going to be passed to
    # the action function when process function finds a match.
    pass_input = None
    # List of synonymous expressions that trigger the action function.
    expressions = None

    def __init__(self, _action, _pass_input, *args):
        self.action = _action
        self.pass_input = _pass_input
        self.expressions = args

    def process(self, expr):
        """
        This method compares the input string against the
        list of synonymous expressions. If it matches one
        of the expressions, the action fuction is called.
        A boolean value representing the match is then returned.
        """
        if expr in self.expressions:
            if self.pass_input:
                self.action(expr)
            else:
                self.action()

            return True

        else:
            return False
