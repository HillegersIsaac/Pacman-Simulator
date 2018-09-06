from grid import Grid
from pacman import PacMan


# Takes any user input and ensures that it is a valid direction to be used for the pacman object
def validate_direction(direction):
    direction_temp = direction.lower()
    if direction_temp == 'NORTH':
        return 0
    elif direction_temp == 'EAST':
        return 1
    elif direction_temp == 'SOUTH':
        return 2
    elif direction_temp == 'WEST':
        return 3
    else:
        return -1


def main():
    # generate our grid.
    grid = Grid()
    pacman = None

    # request and validate PLACE command.
    need_place = True
    while need_place:
        user_input = input("Enter PLACE ('PLACE X,Y,F'): ")
        user_input = user_input.split(" ")
        if str(user_input[0]).lower() == "place" and len(user_input) > 1:
            place_input = user_input[1].split(",")
            if len(place_input) == 3:
                # First two parameters must be integer digits. Not Strings/Floats
                if place_input[0].isdigit() and place_input[1].isdigit():
                    x_val = int(place_input[0])
                    y_val = int(place_input[1])
                    # Must be within this specific grids boundary. Could use validate_position.
                    if (grid.min_boundary <= x_val < grid.max_boundary) and \
                            (grid.min_boundary <= y_val < grid.max_boundary):
                        # Once the first two parameters are verified, verify the direction is legal.
                        direction_val = validate_direction(place_input[2])
                        if direction_val == -1:
                            print("Direction is invalid. Please enter NORTH | EAST | SOUTH | WEST")
                        else:
                            pacman = PacMan(x_val, y_val, direction_val)
                            print(pacman)
                            need_place = False
                    else:
                        print("X,Y positions out of bounds. Please enter within grid parameters.")
                else:
                    print("Invalid X,Y values. They must be positive integer values")
            else:
                print("Invalid number of Place parameters.")
        elif str(user_input[0]) == 'x':
            break

    # request following MOVE | LEFT | RIGHT | REPORT commands.
    need_report = True
    while need_report:
        if pacman is None:
            print("Error involving pacman object creation. Now Exiting.")
            return

        user_input = input("Enter MOVE | LEFT | RIGHT | REPORT: ")

        # Simple breakdown of the required functions with report exiting the user input loop.
        if str(user_input).lower() == 'report':
            print(pacman.report())
            need_report = False
        elif str(user_input).lower() == 'move':
            pacman.move(grid)
        elif str(user_input).lower() == 'left':
            pacman.turn('left')
        elif str(user_input).lower() == 'right':
            pacman.turn('right')
        else:
            print("Please enter a valid action. These are MOVE | LEFT | RIGHT | REPORT")


if __name__ == '__main__':
    main()

