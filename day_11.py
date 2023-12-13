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

csv_file_path = 'day_11_input.csv'
data = read_csv_file(csv_file_path)

#Part 1

#Expand map vertically

empty_row = ""
for char in data[0]:
    empty_row += "."

for y in range(len(data) - 1, -1, -1):
    if "#" not in data[y]:
        data.insert(y+1, empty_row)

#Expand map horizontally

for x in range(len(data[0]) - 1, -1, -1):
    map_column = ""
    for y in range(0, len(data)):
        map_column += data[y][x]
    if "#" not in map_column:
        for y in range(0, len(data)):
            data[y] = data[y][:x] + "." + data[y][x:]

galaxies = {}
galaxy_number = 1

#Identify galaxies

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == "#":
            galaxies[galaxy_number] = [y, x]
            galaxy_number += 1

#Calculate distances

total_distance = 0

for i in range(1, len(galaxies)):
    for j in range(i + 1, len(galaxies) + 1):
        total_distance += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(total_distance)


print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)



