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
    # Evaluation function
    # Determines if the input expression corresponds to the query
    evalfunc = None

    def __init__(self, _action, _pass_input, _evalfunc):
        self.action = _action
        self.pass_input = _pass_input
        self.evalfunc = _evalfunc

    def process(self, expr):
        """
        This methods runs the input expression through the evaluation function
        of this query. If the evaluation function returns true the action function is called.
        Boolean value representing the result of the evaluation function is returned.
        """
        if self.evalfunc(expr):
            if self.pass_input:
                self.action(expr)
            else:
                self.action()

            return True

        else:
            return False
