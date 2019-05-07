from math import sqrt


def calculate_heuristic(neighbor, end):
    # using the raw distance
    x = (neighbor.x, neighbor.y)
    y = (end.x, end.y)
    distance = sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance


class AStar:
    # TODO: Make it a data class
    def __init__(self, grid, end=None, start=None):
        self.grid = grid
        self.end = end
        self.start = start
        self.path = []

        # Assuming to be empty, but perhaps it isn't for scheduling reasons
        self.closed_set = list()

        self.open_set = list()

    def solve(self):
        # if self.pre_run_check():
        """Debugging purposes"""
        self.open_set.append(self.start)
        self.run()

    def pre_run_check(self):
        if self.end is None or self.start is None or not self.open_set:
            return False
        return True

    def run(self):
        while self.open_set:  # checking if we still have something to read from
            lowestIndex = 0
            for i in range(len(self.open_set)):
                if self.open_set[i].f < self.open_set[lowestIndex].f:
                    lowestIndex = i

            if self.open_set[lowestIndex] is self.end:
                self.path = []
                temp = self.open_set[lowestIndex]
                self.path.append([temp.x, temp.y])
                while temp.previous:
                    self.path.append([temp.x, temp.y])
                    temp = temp.previous
                return self.path
            indexes = self.open_set[lowestIndex].get_neighbors(self.grid.rows, self.grid.columns)

            neighbors = list()
            for index in indexes:
                neighbors.append(self.grid[(index[0], index[1])])
            for cell in neighbors:
                if cell not in self.closed_set and cell.accessible:
                    temp_g = cell.g + 1
                    if cell in self.open_set:
                        if temp_g < cell.g:
                            cell.g = temp_g
                    else:
                        cell.g = temp_g

                        self.open_set.append(cell)

                    cell.h = calculate_heuristic(cell, self.end)
                    cell.f = cell.g + cell.h
                    cell.previous = self.open_set[lowestIndex]

            self.closed_set.append(self.open_set[lowestIndex])
            del self.open_set[lowestIndex]

        # make case variable
        print("No Match Found")
