from grid import Grid


class PacMan:

    def __init__(self, x, y, direction):

        self.position = [x, y]
        self.direction = direction

    # Move attempts to move the pacman by requesting from any grid if its move would be legal.
    def move(self, grid):
        temp_position = self.position.copy()
        current_direction = self._get_direction_string()
        if current_direction == "North":
            # North is up, so the Y axis must be scaled positively, knowing that 0,0 is SOUTH WEST
            temp_position[1] += 1
        elif current_direction == "East":
            # East is right, [0, 1, ... , 4], must scale positively along the 'x axis'
            temp_position[0] += 1
        elif current_direction == "South":
            # South is down. Scale negative on the 'y axis'
            temp_position[1] -= 1
        elif current_direction == "West":
            # West is left, negative along the 'x axis'
            temp_position[0] -= 1
        else:
            return "error, current_direction does not match known string constant"

        # Moves the pacman else completely ignores the move as per specifications.
        if grid.validate_position(temp_position[0], temp_position[1]):
            self.position = temp_position
            return "success"
        else:
            return "fail"

    # directions correspond to N = 0, E = 1, S = 2, W = 3.
    # add 1 is turning right
    # minus 1 is turning left.
    def turn(self, direction):
        if direction.lower() == 'left':
            self.direction -= 1
        elif direction.lower() == 'right':
            self.direction += 1

    # Useful for turning the direction value easily into a readable string for feedback.
    def _get_direction_string(self):
        try:
            direction_value = self.direction % 4
        except TypeError:
            return "Invalid direction"

        if direction_value == 0:
            return "North"
        elif direction_value == 1:
            return "East"
        elif direction_value == 2:
            return "South"
        elif direction_value == 3:
            return "West"
        else:
            return "Invalid direction"

    # For testing purposes
    def __str__(self):
        return ("PacMan object facing: " + self._get_direction_string()
                + "\n"
                + "In position: " + str(self.position))

    # For the final output required as per specifications.
    def report(self):
        return "Output: " + str(self.position[0]) + "," + str(self.position[1]) + "," + self._get_direction_string()
