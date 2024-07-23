#!/usr/bin/python3

import random
import neopixel
import time
import board

pixel_pin = board.D18
num_pixels = 256
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

routeColor = (255, 0, 0)
goalColor = (0, 0, 255)
COLOR_EMPTY = (0, 0, 0)

#board_state = [' '] * 256


"""
Breadth First Searching - Anfang
"""

def bfs(start, grid):
    searching = True
    dirs = [(0,1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1), (1, -1)]
    queue = [ start ]
    visited = []
    paths = [] # start = [[][]] ?

    while len(queue) > 0 and searching == True:
        pos = queue.pop()

        for goal in goals:
            if pos == goal:
                searching = False
                break
        else:
            for dx, dy in dirs:
                npos = (pos[0]+dx, pos[1]+dy)
                if npos not in visited and npos[0] in range(16) and npos[1] in range(16):
                    #print(len(visited))
                    paths.append(pos)
                    visited.append(npos)
                    queue.append(npos)

    #retrace path
    srcpath = [pos]
    cpos = pos
    while cpos != start:
        for i in range(len(visited)):
            if visited[i] == cpos:
                srcpath.insert(0, paths[i])
                cpos = paths[i]
                break

    return srcpath

"""
Breadth First Searching - Ende
"""

# Beispielgrid (0 = frei, 1 = Hindernis)
grid = [[0 for _ in range(16)] for _ in range(16)]
start = (int(input("Bitte x Koordinate eingeben")), int(input("Bitte y Koordinate eingeben")))
# Zielpunkte
# //Durch zufall gegebene Ziele// goals = generate_random_goals(num_goals, grid)
goals = [(13, 5), (6, 3), (8, 5), (15, 9)]

#Wasserstellen: Kaiser-Wilhelm-Park, Freibad Aqualip, Palaisgarten, Meschesee
path = bfs(start, grid)

# LEDs entlang des Pfades setzen
print(path)

for (x, y) in path:
    pixels[x+(16*y)] = routeColor
    pixels.show()


time.sleep(3)
# Anzahl der Zielpunkte (1 bis 4)

# Berechne und zeige die Pfade zu jedem Ziel, wenn 42 eingegeben wird
def show_all_routes(start):
    for goal in goals:
        path = bfs(start, grid)
        for (x, y) in path:
            pixels.fill(routeColor)

if int(input("Bitte Zahl eingeben")) == 42:
    show_all_routes(start)
else:
    print("Algorithmus erfolgreich durchgelaufen")

pixels.show()

time.sleep(5)
for i in range(num_pixels):
    pixels[i] = (COLOR_EMPTY)
pixels.show()