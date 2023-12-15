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

def generate_permutations(length):
    characters = [".", "#"]
    permutations = ["".join(p) for p in product(characters, repeat = length)]
    return permutations

def filter_permutations(permutations, character_position, filter_character):
    return [perm for perm in permutations if perm[character_position] == filter_character]

def find_blocks(input_string):
    blocks = []
    current_block = ""
    position = 0

    for char in input_string:
        if char == ".":
            if current_block:
                blocks.append((len(current_block), position - len(current_block)))
                current_block = ""
        else:
            current_block += char

        position += 1

    if current_block:
        blocks.append((len(current_block), position - len(current_block)))

    return blocks

csv_file_path = 'day_12_input.csv'
data = read_csv_file(csv_file_path)

num_arrangements = 0

for line in data:
    row = line.split(" ")
    clues = row[1].split(",")

    print(row[0])

    #Create initial list of possible permutations
    possible_rows = generate_permutations(len(row[0]))

    for i in range(0, len(row[0])):
        if row[0][i] != "?":
            #print(i, row[0][i])
            possible_rows = filter_permutations(possible_rows, i, row[0][i])

    potential_blocks = find_blocks(row[0])

    #print(int(clues[0]), potential_blocks[0][0])

    """
    check_edges = True
    while check_edges == True:
        if int(clues[0]) > potential_blocks[0][0]:
            for i in range(potential_blocks[0][1], potential_blocks[0][0] + potential_blocks[0][1]):
                row[0] = row[0][:i] + "." + row[0][i+1:]
                possible_rows = filter_permutations(possible_rows, i, row[0][1])
                potential_blocks.pop(0)
        else:
            check_edges = False

    check_edges = True
    while check_edges == True:
        if int(clues[-1]) > potential_blocks[-1][0]:
            for i in range(potential_blocks[-1][1], potential_blocks[-1][0] + potential_blocks[-1][1]):
                row[0] = row[0][:i] + "." + row[0][i+1:]
                possible_rows = filter_permutations(possible_rows, i, row[0][i])
                potential_blocks.pop(-1)
        else:
            check_edges = False
    """
    
    for i in range(0, len(possible_rows)):
        current_row = possible_rows[i]
        current_block = 0
        row_score = []
        #if i % 10 == 0:
            #print(i, current_row)

        for j in range(0, len(current_row)):
            if current_row[j] != ".":
                current_block += 1
            elif current_row[j] == "." and current_block > 0:
                row_score.append(str(current_block))
                current_block = 0
        if current_block > 0:
            row_score.append(str(current_block))
    
        if row_score == clues:
            #print(f"MATCH: clues: {clues}; row_score: {row_score}; current_row: {current_row}")
            num_arrangements += 1
        #else:
            #possible_rows.pop(i)
            
    #print(len(possible_rows))

    print(num_arrangements)

    #print(potential_blocks)
    #print(row[0])
    #print(len(possible_rows))
    print("\n")
    






print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)




