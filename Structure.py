# TODO unit tests

class Cell:

    # TODO: Make it a data class
    def __init__(self, x, y, f=0, g=0, h=0):
        self.f = f
        self.g = g
        self.h = h

        self.x = x
        self.y = y
        self.neighbors = []
        self.previous = None


    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, key):
        if key in ['f', 'g', 'h']:
            return self['key']
        return False  # make it either an exception or error

    def get_neighbors(self, x, y):

        # TODO: Loop-based not if statement based

        if self.x < x - 1:
            self.neighbors.append([self.x + 1, self.y])
        if self.x > 0:
            self.neighbors.append([self.x - 1, self.y])
        if self.y < y - 1:
            self.neighbors.append([self.x, self.y + 1])
        if self.y > 0:
            self.neighbors.append([self.x, self.y - 1])
        return self.neighbors
