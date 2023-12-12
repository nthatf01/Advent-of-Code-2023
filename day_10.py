import csv
import time
import sys
import math

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

csv_file_path = 'day_10_input.csv'
data = read_csv_file(csv_file_path)

pipes = {
        "|": [[-1, 0], [1, 0]],     # North, South
        "-": [[0, -1], [0, 1]],     # East,  West
        "L": [[-1, 0], [0, 1]],     # North, East
        "J": [[-1, 0], [0, -1]],    # North, West
        "7": [[0, -1], [1, 0]],     # South, West
        "F": [[0, 1], [1, 0]],      # South, East
        ".": [[0, 0], [0, 0]]       # Empty
        }

starting_point = [-1, -1]

pipe_map = []
current_symbol = ""

#Find the starting point

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == "S":
            starting_point = [y, x]
            pipe_map.append(starting_point)
            print(f"Starting point S found at: ({y}, {x})")
            if data[y][x-1] == "-" or data[y][x-1] == "L" or data[y][x-1] == "F":
                current_position = [y, x - 1]
            elif data[y - 1][x] == "|" or data[y - 1][x] == "7" or data[y - 1][x] == "F":
                current_position = [y - 1, x]
            else:
                current_position = [y, x + 1]
            current_symbol = data[current_position[0]][current_position[1]]
            pipe_map.append(current_position)
            previous_position = starting_point
            break
    if starting_point != [-1, -1]:
        break

returned_to_starting_point = False
steps = 1

print(f"starting_point: {starting_point}; current_position: {current_position}; current_symbol: {current_symbol}")

while returned_to_starting_point == False:
    check_A = pipes[current_symbol][0]
    check_B = pipes[current_symbol][1]

    check_A = [sum(i) for i in zip(current_position, check_A)]
    check_B = [sum(i) for i in zip(current_position, check_B)]

    #print(f"check_A: {check_A}; check_B: {check_B}; current_position: {current_position}; current_symbol: {current_symbol}; previous_position: {previous_position}")
    
    if check_A != previous_position:
        previous_position = current_position
        current_position = check_A
        #print("CHECK A")
    else:
        previous_position = current_position
        current_position = check_B
        #print("CHECK B")

    pipe_map.append(current_position)
    current_symbol = data[current_position[0]][current_position[1]]

    #print(f"starting_point: {starting_point}; current_position: {current_position}; current_symbol: {current_symbol}")

    if current_position != starting_point:
        steps += 1
        if steps >= 140 * 140:
            returned_to_starting_point = True
            break
    else:
        returned_to_starting_point = True
    
    #print(f"check_A: {check_A}; check_B: {check_B}")

print(pipes["|"][0][0])

print(starting_point)

print([sum(x) for x in zip(starting_point, pipes["|"][0])])

print(data[current_position[0]][current_position[1]])

print(steps / 2)





print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)


