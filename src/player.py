class Player:
    self.id = None
    self.stack = 0

    def __init__(self, id, stack):
        self.id = id
        self.stack = stack

    def __str__(self):
        return """
            \tid = {}
            \tstack = {}
        """.format(self.id, self.stack)