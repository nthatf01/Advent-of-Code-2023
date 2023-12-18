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

csv_file_path = 'day_13_input.csv'
data = read_csv_file(csv_file_path)

line_index = 0
pattern_matrix = []

total = 0
total_rows = 0
total_columns = 0

for row_count, line in enumerate(data):
    if line == "" or row_count == len(data) - 1:
        if row_count == len(data) - 1:
            pattern_matrix.append(data[row_count])
        #print(pattern_matrix)
        #print("\n")

        horizontal_index = 0
        vertical_index = 0

        #Horizontal line of reflection check
        for y in range(0, len(pattern_matrix) - 1):
            #print(f"y: {y}")
            if pattern_matrix[y] == pattern_matrix[y + 1]:
                #print(f"Horizontal match: {y} {pattern_matrix[y]} {pattern_matrix[y+1]}")
                top_height = y + 1
                bottom_height = len(pattern_matrix) - (y + 1)
                horizontal_index = 0
                if top_height >= bottom_height:
                    horizontal_index = 0
                    height_cursor = y
                    for y2 in range(y + 1, len(pattern_matrix)):
                        if pattern_matrix[y2] == pattern_matrix[height_cursor]:
                            horizontal_index = y + 1
                            #print(f"Still matched: {pattern_matrix[y2]}, {pattern_matrix[height_cursor]}")
                        else:
                            #print("Match broken!")
                            horizontal_index = 0
                            break
                        height_cursor -= 1
                    if horizontal_index > 0:
                        break
                else:
                    horizontal_index = 0
                    height_cursor = y + 1
                    for y2 in range(y, -1, -1):
                        #print(f"y: {y}, y2: {y2}")
                        if pattern_matrix[y2] == pattern_matrix[height_cursor]:
                            horizontal_index = y + 1
                            #print(f"Still matched: {pattern_matrix[y2]}, {pattern_matrix[height_cursor]}")
                        else:
                            #print("Match broken!")
                            horizontal_index = 0
                            break
                        height_cursor += 1
                    if horizontal_index > 0:
                        break

        print(f"Horizontal reflection at: {horizontal_index}")

        #Vertical line of reflection check


        #Transpose matrix
        column_cursor = 0
        transposed_matrix = []


        for x in range(0, len(pattern_matrix[0])):
            temp_column = ""
            for y in range(0, len(pattern_matrix)):
                temp_column += pattern_matrix[y][x]
                #print(x, y, temp_column)
            transposed_matrix.append(temp_column)

        #print(transposed_matrix)
        pattern_matrix = transposed_matrix

        for y in range(0, len(pattern_matrix) - 1):
            #print(f"y: {y}")
            if pattern_matrix[y] == pattern_matrix[y + 1]:
                #print(f"Vertical match: {y} {pattern_matrix[y]} {pattern_matrix[y+1]}")
                top_height = y + 1
                bottom_height = len(pattern_matrix) - (y + 1)
                vertical_index = 0
                if top_height >= bottom_height:
                    #print(top_height, bottom_height)
                    vertical_index = 0
                    height_cursor = y
                    for y2 in range(y + 1, len(pattern_matrix)):
                        if pattern_matrix[y2] == pattern_matrix[height_cursor]:
                            vertical_index = y + 1
                            #print(f"Still matched: {pattern_matrix[y2]}, {pattern_matrix[height_cursor]}")
                        else:
                            #print("Match broken!")
                            vertical_index = 0
                            break
                        height_cursor -= 1
                    if vertical_index > 0:
                        break
                else:
                    vertical_index = 0
                    height_cursor = y + 1
                    for y2 in range(y, -1, -1):
                        if pattern_matrix[y2] == pattern_matrix[height_cursor]:
                            vertical_index = y + 1
                            #print(f"Still matched: {pattern_matrix[y2]}, {pattern_matrix[height_cursor]}")
                        else:
                            #print("Match broken!")
                            vertical_index = 0
                            break
                        height_cursor += 1
                    if vertical_index > 0:
                        break

        print(f"Vertical reflection at: {vertical_index}")
        print(horizontal_index, vertical_index)
        print(f"current row total: {((horizontal_index * 100) + (vertical_index))}")

        total += ((horizontal_index * 100) + (vertical_index))
                        
        
        pattern_matrix = []
    else:
        pattern_matrix.append(line)



print(f"Total columns/rows: {total}")



print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)




