class expression:
    action = None
    matches = None

    def __init__(self, callback, *args):
        self.action = callback
        self.matches = args

    def compare(self, expr):
        return expr in self.matches
