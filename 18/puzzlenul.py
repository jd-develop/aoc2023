#!/usr/bin/env python3 # -*- coding:utf-8 -*-
from pprint import pprint

with open("input", "r+", encoding="utf-8") as input_f:
    input_list = input_f.readlines()


def parse(puzzle_input: list[str]):
    """Return a list of tuples (str, int, str), for instance ("R", 6, "#70c710")"""
    list_to_return = []
    for line in puzzle_input:
        if line == "\n":
            continue
        line = line.split()
        direction = line[0]
        meters = int(line[1])
        color = line[2]
        if color.endswith("\n"):
            color = color[:-1]
        color = color[1:-1]
        list_to_return.append((direction, meters, color))
    return list_to_return


def to_terrain(parsed_input):
    """Return the terrain"""
    list_of_points = [(0, 0)]
    current_point = (0, 0)
    perimeter = 0
    for direction, meters, _ in parsed_input:
        perimeter += meters
        for i in range(meters):
            x, y = current_point
            if direction == "U":
                x -= 1
            elif direction == "D":
                x += 1
            elif direction == "L":
                y -= 1
            elif direction == "R":
                y += 1
            current_point = (x, y)
            list_of_points.append(current_point)
    min_x = min(list_of_points, key=lambda e: e[0])[0]
    min_y = min(list_of_points, key=lambda e: e[1])[1]
    if min_x < 0:
        list_of_points = [(x-min_x, y) for x, y in list_of_points]
    if min_y < 0:
        list_of_points = [(x, y-min_y) for x, y in list_of_points]

    max_x = max(list_of_points, key=lambda e: e[0])[0]
    max_y = max(list_of_points, key=lambda e: e[1])[1]
    terrain = [["."]*(max_y+1) for i in range(max_x+1)]
    for x, y in list_of_points:
        terrain[x][y] = "#"
    return terrain


def area(terrain):
    """Return the total area of the terrain"""
    total = 0
    for row in terrain:
        count = 0
        inside = False
        for cell in row:
            if cell == "#":
                count += 1
                print("\033[91m#\033[0m", end="")
                total += 1
            else:
                if (count != 0 and not inside) or (count == 0 and inside):
                    inside = True
                    count = 0
                    print("\033[92m.\033[0m", end="")
                    total += 1
                else:
                    print(".", end="")
        print()
    return total


parsed_list = parse(input_list)
terrain = to_terrain(parsed_list)
print(area(terrain))
# print(area([
#     "...###############...",
#     "...#.............#...",
#     "...##.....###....#...",
#     "....#.....#.#....#...",
#     "....#######.#....#...",
#     "............######..."
# ]))

