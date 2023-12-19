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




csv_file_path = 'day_14_input.csv'
data = read_csv_file(csv_file_path)

tilted_data = []

#Initialize the empty tilted data list for use later
for i in range(0, len(data)):
    tilted_data.append("")

#Tilt the data upwards
for x in range(0, len(data[0])):
    temp_column = ""
    column_sections = []
    sorted_column = ""
    
    for y in range(0, len(data)):
        temp_column += data[y][x]

    column_sections = temp_column.split("#")

    for i, section in enumerate(column_sections):
        sorted_column += "".join(sorted(section, key = lambda k: (k != "O", k)))

        if i != len(column_sections) - 1:
            sorted_column += "#"
            
    for i in range(0, len(sorted_column)):
        tilted_data[i] += sorted_column[i]

northern_load = 0

for i in range(0, len(tilted_data)):
    northern_load += tilted_data[i].count("O") * (len(tilted_data) - i)

print(f"Total load on northern beams: {northern_load}")
        








print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)




