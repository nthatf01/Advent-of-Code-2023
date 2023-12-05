import csv
import re

def read_csv_file(file_path):
    data_list = []

    try:
        with open(file_path, mode = 'r', encoding = 'utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Skip the header row if it exists
            # header = next(csv_reader, None)

            for row in csv_reader:
                data_list.append(str(row)[2:-2])
                
        return data_list

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

csv_file_path = 'day_4_input.csv'
data = read_csv_file(csv_file_path)

cards = []
for line in data:
    cards.append(1)

def prepare_numbers(line):
    #remove white space entries
    line = list(filter(lambda x: x != " ", line))
    line = list(filter(lambda x: x != "", line))

    return line

line_number = 0
total_cards = 0

for line in data:
    current_matches = 0
    print(line)
    #print(line[line.find(":")+1:line.find("|")])
    #grab the winning numbers
    winning_numbers = (line[line.find(":")+1:line.find("|")]).strip().split(" ")
    prepare_numbers(winning_numbers)
    #grab the have numbers
    have_numbers = (line[line.find("|")+1:]).strip().split(" ")
    prepare_numbers(have_numbers)

    for number in have_numbers:
        #print(f"Current have number: {number}")
        if number in winning_numbers and number.isdigit():
            #print(f"Current have number: {number}")
            current_matches += 1
    print(f"Matches this row: {current_matches}")

    if current_matches >= 1:
        for i in range(line_number + 1, line_number + current_matches + 1):
            cards[i] += cards[line_number]
            print(f"Number of new cards added to row {i} is: {cards[i]}")
    total_cards += cards[line_number]
    print(f"The number of cards this row: {cards[line_number]}")
    print(f"The total number of cards as of this row: {total_cards}")
    line_number += 1

