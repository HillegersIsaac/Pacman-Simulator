class Grid:

    # Allows customizable grid layouts,
    GRID_MIN = 0
    GRID_SIZE = 5

    def __init__(self):
        self.min_boundary = self.GRID_MIN
        self.max_boundary = self.GRID_SIZE

    # Validates to a pacman object if it is within the specified boundary
    def validate_position(self, x, y):
        valid = False

        if (self.min_boundary <= x < self.max_boundary) \
                and (self.min_boundary <= y < self.max_boundary):
            valid = True

        return valid

    # For testing purposes.
    def __str__(self):
        return 'height:' + str(self.max_boundary) + '\n' + 'width:' + str(self.max_boundary)
