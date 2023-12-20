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

csv_file_path = 'day_15_input.csv'
data = read_csv_file(csv_file_path)

hash_steps = []
hash_steps = data[0].split(",")

total_value = 0

for step in hash_steps:
    current_value = 0
    for char in step:
        #Increase current value by ASCII code value
        current_value += ord(char)
        #Increase current value by 17x
        current_value *= 17
        #Decrease current value to modulo 256
        current_value %= 256
    total_value += current_value

print(f"Sum of hash values: {total_value}")




print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)




