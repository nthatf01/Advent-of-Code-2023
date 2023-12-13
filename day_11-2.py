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

#Part 2

#Map empty rows

empty_rows = {}
cumulative_empty = 0

for y in range(0, len(data)):
    if "#" not in data[y]:
        cumulative_empty += 1
    empty_rows[y] = cumulative_empty

#Map empty columns

empty_columns = {}
cumulative_empty = 0

for x in range(0, len(data[0])):
    map_column = ""
    for y in range(0, len(data)):
        map_column += data[y][x]
    if "#" not in map_column:
        cumulative_empty += 1
    empty_columns[x] = cumulative_empty

galaxies = {}
galaxy_number = 0

#Identify galaxies

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == "#":
            galaxies[galaxy_number] = [y, x]
            galaxy_number += 1

#Calculate distances

total_distance = 0

for i in range(0, len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        total_distance += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]) + (abs((empty_rows[galaxies[i][0]] - empty_rows[galaxies[j][0]])) * 999999) + (abs((empty_columns[galaxies[i][1]] - empty_columns[galaxies[j][1]])) * 999999)

print(total_distance)


print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)



