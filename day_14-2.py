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
data_history = []
data_single = "".join("".join(map(str, sublist)) for sublist in data)
data_history.append(data_single)
match_found = False
spin_count = 0
spin_match = 0

#Initialize the empty tilted data list for use later
for i in range(0, len(data)):
    tilted_data.append("")


while match_found == False and spin_count < 1000:
    spin_count += 1
    
    #Tilt the data northward
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

    #Tilt the data westward
    for y in range(0, len(tilted_data)):
        sorted_row = ""
        row_sections = tilted_data[y].split("#")

        for i, section in enumerate(row_sections):
            sorted_row += "".join(sorted(section, key = lambda k: (k != "O", k)))

            if i != len(row_sections) - 1:
                sorted_row += "#"
                
        tilted_data[y] = sorted_row

    #Tilt the data southward

    tilted_data2 = []
    for i in range(0, len(tilted_data)):
        tilted_data2.append("")


    for x in range(0, len(tilted_data[0])):
        temp_column = ""
        column_sections = []
        sorted_column = ""
        
        for y in range(0, len(tilted_data)):
            temp_column += tilted_data[y][x]

        column_sections = temp_column.split("#")

        for i, section in enumerate(column_sections):
            sorted_column += "".join(sorted(section, key = lambda k: (k != ".", k)))

            if i != len(column_sections) - 1:
                sorted_column += "#"
        
        for i in range(0, len(sorted_column)):
            tilted_data2[i] += sorted_column[i]

    #Tilt the data eastward
    for y in range(0, len(tilted_data2)):
        sorted_row = ""
        row_sections = tilted_data2[y].split("#")

        for i, section in enumerate(row_sections):
            sorted_row += "".join(sorted(section, key = lambda k: (k != ".", k)))

            if i != len(row_sections) - 1:
                sorted_row += "#"
                
        tilted_data[y] = sorted_row

    """
    for i in range(0, len(tilted_data)):
        print(tilted_data[i], " - ", tilted_data[i].count("O"), " * ", len(tilted_data) - i)

    print("\n")

    northern_load = 0
    

    for i in range(0, len(tilted_data)):
        northern_load += tilted_data[i].count("O") * (len(tilted_data) - i)
    print(northern_load)
    """
    
    data_single = "".join("".join(map(str, sublist)) for sublist in tilted_data)

    
    if data_single in data_history:
        print("MATCH")
        #print(spin_match)
        print(spin_count, data_history.index(data_single), spin_count - data_history.index(data_single))
        #print(tilted_data)
        match_found = True
    else:
        data_history.append(data_single)
        spin_match = spin_count
        

    for i in range(0, len(data)):
        data[i] = tilted_data[i]
        tilted_data[i] = ""
        tilted_data2[i] = ""
    



#print(data_history)


billion_data = []
#billion_data_index = (1000000000 % (spin_count - data_history.index(data_single)))
billion_data_index = 129


#pre_cycle = data_history.index(data_single) - 1
#cycle_freq = spin_count - data_history.index(data_single)
#p1 = 1000000000 - pre_cycle

#p2 = p1 % cycle_freq

#p3 = cycle_freq - p2 + pre_cycle

#p4 = 132

#print(p3)

for j in range(103, 142):
    billion_data = []
    northern_load = 0
    for i in range(0, 100):
        billion_data.append(data_history[127][i*100:(i*100+100)])
    for i in range(0, len(billion_data)):
        northern_load += billion_data[i].count("O") * (len(billion_data) - i)

    print(f"{127} - Total load on northern beams: {northern_load}")


    

#billion_data = data_history[billion_data_index]


print(billion_data_index)
print(billion_data)



northern_load = 0

for i in range(0, len(billion_data)):
    northern_load += billion_data[i].count("O") * (len(billion_data) - i)

print(f"Total load on northern beams: {northern_load}")









print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)




