import csv
import time
import sys
import math
from itertools import product

startTime = time.perf_counter()

def read_csv_file(file_path):
    data_list = []

    try:
        with open(file_path, mode = 'r', encoding = 'utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                data_list.append(str(row)[2:-2])
                
        return data_list

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def calculate_energized_cells(map_grid, initial_beam):

    beam_queue = []
    beam_queue.append(initial_beam)
    energized_cells = []
    next_pos_y = 0
    next_pos_x = 0
    cell_signature = ""
    cell_history = []
    energized_cells = []
    
    while len(beam_queue) > 0:
        current_beam = beam_queue.pop()
        #print(current_beam)
        next_pos_y = current_beam["Y"] + traversal[current_beam["D"]][0]
        next_pos_x = current_beam["X"] + traversal[current_beam["D"]][1]

        #Check if beam would travel out of bounds
        if next_pos_y < 0 or next_pos_y >= len(map_grid) or next_pos_x < 0 or next_pos_x >= len(map_grid[0]):
            continue
        
        cell_signature = str(next_pos_y) + "," + str(next_pos_x) + "," + current_beam["D"]

        #Mark cell as energized if needed
        if cell_signature[:-2] not in energized_cells:
            energized_cells.append(cell_signature[:-2])

        #End iteration if signature in history (on a known previous path)
        if cell_signature in cell_history:
            continue
        
        elif cell_signature not in cell_history:
            cell_history.append(cell_signature)

            cell = map_grid[next_pos_y][next_pos_x]

            if cell == ".":
                temp_beam = {
                    "D": (current_beam["D"]),
                    "Y": (next_pos_y),
                    "X": (next_pos_x)
                    }
                beam_queue.append(temp_beam)
            elif cell != ".":
                for i in range(0, len(mirrors[cell][current_beam["D"]])):
                    temp_beam = {
                    "D": (mirrors[cell][current_beam["D"]][i]),
                    "Y": (next_pos_y),
                    "X": (next_pos_x)
                    }
                    beam_queue.append(temp_beam)
        #print(f"Current location: {current_beam['Y']}, {current_beam['X']}")
        
    #print(next_pos_y, next_pos_x, cell_signature)
    #print(cell_history)
    #print(f"Number of energized cells: {len(energized_cells)}")
    return len(energized_cells)



csv_file_path = 'day_16_input.csv'
data = read_csv_file(csv_file_path)
csv_file_path = 'day_16_test_input.csv'
test_data = read_csv_file(csv_file_path)
mirror_grid = data

#Replace backslashes with greater-than signs
for i in range(0, len(mirror_grid)):
    mirror_grid[i] = mirror_grid[i].replace('\\', '>')
    mirror_grid[i] = mirror_grid[i].replace('>>', '>')

traversal = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1)
    }

mirrors = {
    "/": {
        "N": ("E"),
        "E": ("N"),
        "S": ("W"),
        "W": ("S")
        },
    ">":{
        "N": ("W"),
        "E": ("S"),
        "S": ("E"),
        "W": ("N")
        },
    "|":{
        "N": ("N"),
        "E": ("N", "S"),
        "S": ("S"),
        "W": ("N", "S")
        },
    "-":{
        "N": ("W", "E"),
        "E": ("E"),
        "S": ("W", "E"),
        "W": ("W")
        }
    }

max_energized = 0
temp_energized = 0


#Check top row
for i in range(0, len(mirror_grid[0])):
    beam_init = {
        "D": ("S"),
        "Y": (-1),
        "X": (i)
        }
    
    temp_energized = calculate_energized_cells(mirror_grid, beam_init)
    if temp_energized > max_energized:
        max_energized = temp_energized

#Check bottom row
for i in range(0, len(mirror_grid[0])):
    beam_init = {
        "D": ("N"),
        "Y": (len(mirror_grid)),
        "X": (i)
        }
    
    temp_energized = calculate_energized_cells(mirror_grid, beam_init)
    if temp_energized > max_energized:
        max_energized = temp_energized

#Check left column
for i in range(0, len(mirror_grid)):
    beam_init = {
        "D": ("E"),
        "Y": (i),
        "X": (-1)
        }
    
    temp_energized = calculate_energized_cells(mirror_grid, beam_init)
    if temp_energized > max_energized:
        max_energized = temp_energized

#Check right column
for i in range(0, len(mirror_grid)):
    beam_init = {
        "D": ("W"),
        "Y": (i),
        "X": (len(mirror_grid[0]))
        }
    
    temp_energized = calculate_energized_cells(mirror_grid, beam_init)
    if temp_energized > max_energized:
        max_energized = temp_energized


print(f"Maximum possible energized cells: {max_energized}")


print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)




