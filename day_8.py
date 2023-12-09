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

csv_file_path = 'day_8_input.csv'
data = read_csv_file(csv_file_path)

nodes = []
pairs = []

instructions = "LRRRLRRRLRRLRLRRLLRRLLRLRRRLRRLRRRLRRLLRLRLRRRLRLLRRRLLRLRRRLRLRRRLRRRLRRRLRRRLRLLLRRRLRRLRRLRRRLRLRLRRLRLRRRLRLRLRLRRRLRRLRLRRRLRRLRRRLRRLLRRRLLRLLRLRRRLRLLRRLLRRRLRLLRRLRLRRLRRRLRLRLRLLRLRRRLRRRLRLLLRRRLRLRRRLRRLRRLLLLRLRRRLRLRRRLLRRRLRRRLRRRLLLRLRLRLLLLRRRLRRLRRRLRLRLRLRRRLRLRRRR"

for line in data:
    nodes.append(line[0:3])
    pairs.append(line[7:15].split(", "))

node_dict = dict(zip(nodes, pairs))    

#Part 1

current_node = "AAA"
found_ZZZ = False

steps = 0

while found_ZZZ == False:

    for char in instructions:
        steps += 1
        if char == "L":
            current_node = node_dict[current_node][0]
        else:
            current_node = node_dict[current_node][1]
        if current_node == "ZZZ":
            found_ZZZ = True
            break

print(f"Number of steps required to find ZZZ: {steps}")

#Part 2

steps_list = []
steps = 0

for node in node_dict:
    steps = 0
    found_Z = False
    if node[2] != "A":
        continue
    else:
        current_node = node
        while found_Z == False:

            for char in instructions:
                steps += 1
                if char == "L":
                    current_node = node_dict[current_node][0]
                else:
                    current_node = node_dict[current_node][1]
                if current_node[2] == "Z":
                    steps_list.append(int(steps))
                    found_Z = True
                    break
                
steps = math.lcm(*steps_list)
print(f"Number of steps required to find Z: {steps}")

print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
