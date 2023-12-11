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
                data_list.append(str(row)[2:-2].split(" "))
                
        return data_list

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

csv_file_path = 'day_9_input.csv'
data = read_csv_file(csv_file_path)

#Part 1

total_value = 0
total_value2 = 0

for line in data:
    current_line = line
    row_count = 0
    triangle_list = []
    #print(f"Initial line: {line}")
    #Create lower row until n is found
    for i in range (len(line)-1, -1, -1):
        #print(f"Outer i value: {i}")
        row_constructor = ""
        for j in range(i, 0, -1):
            #print(f"Inner j value: {j}")
            row_constructor += str(int(current_line[j]) - int(current_line[j - 1])) + " "
        row_constructor = row_constructor[0:-1]
        #print(f"row_constructor value: {row_constructor}")
        triangle_list.append(row_constructor.split(" "))
        #print(f"triangle_list: {triangle_list[row_count]}")

        #Make sure to reverse list before next iteration
        current_line = triangle_list[row_count][::-1]
        #print(triangle_list[row_count][::-1])
        row_count += 1
        #print(current_line)
        if len(set(current_line)) == 1:
            #print(set(current_line))
            break
        
    #Calculate next value in history
    next_value = int(line[20])
    for i in range(0, row_count):
        #print(triangle_list[i][0])
        next_value += int(triangle_list[i][0])

    total_value += next_value

    #Part 2

    previous_value = int(line[0])
    temp_value = 0
    for i in range(row_count - 1, -1, -1):
        #print(f"row_count - 1: {row_count - 1 - i}; triangle_list: {triangle_list[i][len(triangle_list[i])-1]}")
        temp_value = int(triangle_list[i][len(triangle_list[i])-1]) - temp_value
    previous_value = previous_value - temp_value
    #print(previous_value)
    
    total_value2 += previous_value


print(total_value)
print(total_value2)


print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)

