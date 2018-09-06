from grid import Grid
from pacman import PacMan


# 0 = NORTH
# 1 = EAST
# 2 = SOUTH
# 3 = WEST

def provided_test_case_1():
    grid = Grid()
    pacman = PacMan(0, 0, 0)

    pacman.move(grid)

    test_result = pacman.report()
    if test_result == "Output: 0,1,North":
        print("Test case 1: Success | Result, " + test_result)
    else:
        print("Incorrect result achieved: " + test_result)


def provided_test_case_2():
    grid = Grid()
    pacman = PacMan(0, 0, 0)
    pacman.turn("left")

    test_result = pacman.report()
    if test_result == "Output: 0,0,West":
        print("Test case 2: Success | Result, " + test_result)
    else:
        print("Incorrect result achieved: " + test_result)


def provided_test_case_3():
    grid = Grid()
    pacman = PacMan(1, 2, 1)

    pacman.move(grid)
    pacman.move(grid)
    pacman.turn("left")
    pacman.move(grid)

    test_result = pacman.report()
    if test_result == "Output: 3,3,North":
        print("Test case 3: Success | Result, " + test_result)
    else:
        print("Incorrect result achieved: " + test_result)


def test_case_4():
    grid = Grid()
    pacman = PacMan(0, 0, 0)

    pacman.move(grid)
    pacman.move(grid)
    pacman.turn("left")
    pacman.move(grid)

    test_result = pacman.report()
    if test_result == "Output: 0,2,West":
        print("Test case 3: Success | Result, " + test_result)
    else:
        print("Incorrect result achieved: " + test_result)

# TO ADD
# possible pacman unit tests include,
# [North, East, South, West] in/out of bounds
# possible grid unit tests include,
# X,Y coordinates in/out of bounds


if __name__ == '__main__':
    provided_test_case_1()
    provided_test_case_2()
    provided_test_case_3()
    test_case_4()

