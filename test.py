# This is a sample Python script.
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image

from matplotlib.patches import Circle


def read_map(file):
    # read the map image file
    map_img = cv2.imread(file, 0)
    print("Shape of the loaded image is", map_img.shape)

    # Convert to binary. Values are either 0 (black/obstacle) or 255 (white/traversable space)
    _, map_binary = cv2.threshold(map_img, 127, 255,
                                  cv2.THRESH_BINARY)  # cv.threshold(src, thresholdValue, maxValue, threshold type)

    # view map - comment out if viewing not necessary
    # cv2.imshow("Initial map", map_binary)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return map_binary


def animate(map, path):
    # image = np.array(map)
    # print(image.shape)  # prints the dimensions of the image

    image = cv2.cvtColor(map, cv2.COLOR_GRAY2RGB)

    for x, y in path:
        cv2.circle(image, (x, y), 3, (0, 0, 255), 3)
        cv2.imshow("Path animation", image)
        cv2.waitKey(100)  # waiting using waitKey method if 0

    # cv2.destroyAllWindows()
    return image


def obstacle(point, map_binary):
    print('MAP ::: ', type(map_binary))
    print('PONTS ::: ', point[0], point[1])
    reshaped = np.asarray(map_binary)
    print('RESHAPED ::: ', type(reshaped), reshaped)
    test = (map_binary[point[0]][point[1]]).astype(int)
    print("TEST ::: ", type(test), test)
    print('is correct? ?? ', test == np.int32(0))
    return test == 0


def moveLeft(x, y):
    return [x - 1, y]


def moveRight(x, y):
    return [x + 1, y]


def moveUp(x, y):
    return [x, y - 1]


def moveDown(x, y):
    return [x, y + 1]


def move(x, y, map_binary):
    print('input ::: ', x, y)
    move_left = moveLeft(x, y)
    move_right = moveRight(x, y)
    move_up = moveUp(x, y)
    move_down = moveDown(x, y)

    if (not obstacle(move_up, map_binary)):
        print("I MOVE UP")
        return move_up

    elif (not obstacle(move_right, map_binary)):
        return move_right

    elif (not obstacle(move_down, map_binary)):
        print("I MOVE DOWN")
        return move_down

    elif (not obstacle(move_left, map_binary)):
        return move_left


def bug0(start, goal, map):
    # print("This is bug0")

    # Array for the path points to plot.
    path = []

    # Start point for the bug algorithm
    x, y = start

    print("Start:", x, y)

    print("Goal:", goal[0], goal[1])

    # TODO Plot Start and goal in image

    # x,y = 0

    # Checks if the starting point is an obstacle map[x][y] == 0
    if map_binary[x][y] == 0:
        print("cant start inside obstacle")
        return

    print(map_binary[goal[0]][goal[1]])
    if map[goal[0], goal[1]] == 0:
        print("can't end inside wall")
        return

    # Some code which determine the direction from the known goal
    i = 0

    while (x != goal[0] and y != goal[1]):

        # Saves the path coordinates for the animation functions.
        prevX = x
        prevY = y

        x, y = move(x, y, map_binary)
        i += 1
        if ((x, y) not in path):
            path.append((x, y))
        else:
            break
        print("MAPVALUE :::: ", map_binary[x][y])
        if map_binary[x][y] == 225:
            break
        if i > 45:
            break
        # if map[x][y] != 0:          # No obstacle keep going towards the goal
        #     x += 1
        #     y += 1

        # elif map[x][y] == 0:      # Checks coordinate above
        #     x += 1
        #     y -= 1

        # elif map[x-1][y+1] != 0:    # Checks coordinate in left corner
        #     x += 1

        # elif map[x+1][y] != 0:      # Checks coordinate to the right
        #     y -= 1

        # elif map[x-1][y] == 0:
        #     y -= 1

        # elif map[x+1][y-1] == 0:
        #     y -= 1

        # elif map[x][y-1] == 0:
        #     y -= 1

    return path


def bug1(start, goal, map):
    print("This is bug1")

    # Array for the path points to plot.
    path = []

    # Start point for the bug algorithm
    x, y = start

    # Checks if the starting point is an obstacle
    if map[x][y] == 0:
        print("cant start inside obstacle")
        return

    if map[goal[0]][goal[1]] == 0:
        print("can't end inside wall")
        return

    while (x != goal[0] and y != goal[1]):
        path.append((x, y))
        # Some moving logic
        x += 1
        y += 1

    return path


def bug2(start, goal, map):
    print("This is bug2")

    # Array for the path points to plot.
    path = []

    # Start point for the bug algorithm
    x, y = start

    # Checks if the starting point is an obstacle
    if map[x][y] == 0:
        print("cant start inside obstacle")
        return

    if map[goal[0]][goal[1]] == 0:
        print("can't end inside wall")
        return

    return path


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # adapt for desired map file
    map_file = 'maze-32-32-4.png'
    map_binary = read_map(map_file)

    # print(map)

    # Test path for function.
    # path = [(120,120),(120,120),(120,120),(130,130),(110,110)]
    print('map ::: ', map_binary)
    # animate(map,path)
    path = bug0((250, 250), (500, 500), map_binary)

    # print(path)
    animate(map_binary, path)

    # path = bug1((0, 0), (10, 10), map)
    # animate(map, path)

    # path = bug2((0, 0), (10, 10), map)
    # animate(map, path