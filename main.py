# This is a sample Python script.
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image

from matplotlib.patches import Circle

def read_map(file):
    # read the map image file
    map_img = cv2.imread(file, 2)
    print("Shape of the loaded image is", map_img.shape)

    #Convert to binary. Values are either 0 (black/obstacle) or 255 (white/traversable space)
    _, map_binary = cv2.threshold(map_img, 127, 255, cv2.THRESH_BINARY) #cv.threshold(src, thresholdValue, maxValue, threshold type)

    #print(map_binary)
    # view map - comment out if viewing not necessary
    cv2.imshow("Initial map", map_binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return map_binary

def animate(map,path):

    #image = np.array(map)
    #print(image.shape)  # prints the dimensions of the image
    image = cv2.cvtColor(map, cv2.COLOR_GRAY2RGB)

    cv2.imshow("Path animation", image)
    cv2.waitKey(1000)  # waiting using waitKey method if 0

    for x,y in path:
        cv2.circle(image, (x, y), 3, (0, 0, 255), 3)
        cv2.imshow("Path animation", image)
        cv2.waitKey(10)  # waiting using waitKey method if 0

    cv2.destroyAllWindows()
    return image

def obstacle(x,y,map):
    if map[0][1] == 0:
        print("There is no obstacle")
        return 0
    else:
        print("There is an obstacle")
        return 1

def bug0(start,goal,map):
    #Array for the path points to plot.
    path = []

    #print("Obs",map[251][251])
    # Start point for the bug algorithm
    x, y = start
    gx, gy = goal
    path.append((x, y))
    print("Start:",x,y)
    print("Goal:",gx,gy)

    # TODO Plot Start and goal in image
    # enable color for drawing on map
    st = (start[0],start[1])
    go = (goal[0],goal[1])
    #cv2.circle(map, st, 3, (0, 0, 255), 3)
    #cv2.circle(map, go, 3, (0, 0, 255), 3)

    # Checks if the starting point is an obstacle map[x][y] == 0
    if map[x][y] == 0:
        print("cant start inside obstacle")
        return
    if map[gx,gy] == 0:
        print("can't end inside wall")
        return

    # Some code which determine the direction from the known goal

    while (x != gx and y != gy):

        path.append((x, y))
        if map[x][y] != 0:          # No obstacle keep going towards the goal
            x += 1
            y += 1


        elif map[x][y] == 0:
            x -=1
            path.append((x, y))
            print("obstacle",x,y)









        # elif map[x+1][y] != 0:      # Checks coordinate above
        #     x += 1
        #
        # elif map[x][y+1] != 0:    # Checks coordinate in under
        #     y += 1
        #
        # elif map[x-1][y+1] == 0:    # Check left corner
        #     x += 1
        #     y += 1
        #
        # elif map[x-1][y] != 0:
        #     x -= 1
        #
        # elif map[x-1][y-1] != 0:
        #     x -= 1
        #     y -= 1
        #
        # elif map[x][y-1] != 0:
        #     y -= 1
        #
        # elif map[x+1][y-1] != 0:
        #     x += 1
        #     y -= 1
    path.append((goal[0],goal[1]))
    print(path)
    return path

def bug1(start, goal, map):
    print("This is bug1")

    #Array for the path points to plot.
    path = []

    #Start point for the bug algorithm
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

def bug2(start,goal,map):
    print("This is bug2")

    print(map)

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
    map = read_map(map_file)

    #print(map)

    # Test path for function.
    #path = [(120,120),(120,120),(120,120),(130,130),(110,110)]

    #animate(map,path)
    path = bug0((250, 250), (500, 500), map)
    animate(map, path)

    # path = bug1((0, 0), (10, 10), map)
    # animate(map, path)

    #path = bug2((250, 250), (500, 500), map)
    # animate(map, path)


