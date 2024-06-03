#!/usr/bin/python3
"""alu-interview"""


def rain(walls):
    if not walls:  # If the list is empty, return 0
        return 0

    total_water = 0
    # Stores the maximum wall height to the left of each position
    left_max = [0] * len(walls)
    # Stores the maximum wall height to the right of each position
    right_max = [0] * len(walls)
    # Calculate the maximum wall height to the left of each position
    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Calculate the maximum wall height to the right of each position
    right_max[-1] = walls[-1]
    for i in range(len(walls) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate the amount of water trapped at each position
    for i in range(len(walls)):
        water_level = min(left_max[i], right_max[i]) - walls[i]
        if water_level > 0:
            total_water += water_level

    return total_water
