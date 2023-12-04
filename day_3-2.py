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

csv_file_path = 'day_3_input.csv'
data = read_csv_file(csv_file_path)

regex_pattern = re.compile(r'[*]')

#print(data[4])

#Part 2

line_num = 0
line = data[4]

number_of_gears = 0
gear1 = 0
gear2 = 0
gear_ratio = 0
gear_sum = 0

part_sum = 0
check_other_diagonal = False

for line in data:
    print(f"Line number: {line_num}")
    print(f"Line: {line}")
    char_num = 0
    for char in line:
        number_of_gears = 0
        gear1 = 0
        gear2 = 0
        if bool(regex_pattern.search(char)) == True:
            print(f"Match found: {char}")
            
            #Check left
            if line[char_num - 1].isdigit():
                if line[char_num - 2].isdigit():
                    if line[char_num - 3].isdigit():
                        check_num = line[char_num - 3] + line[char_num - 2] + line[char_num - 1]
                    else:
                        check_num = line[char_num - 2] + line[char_num - 1]
                else:
                    check_num = line[char_num - 1]
                part_sum += int(check_num)
                #print(f"Left part number: {check_num}")
                number_of_gears += 1
                print(f"Left gear found: {check_num}")
                print(f"Number of gears: {number_of_gears}")
                if number_of_gears == 1:
                    gear1 = int(check_num)
                elif number_of_gears == 2:
                    gear2 = int(check_num)
                elif number_of_gears >= 3:
                    gear1 = 0
                    gear2 = 0
            
            #Check right
            if line[char_num + 1].isdigit():
                if line[char_num + 2].isdigit():
                    if line[char_num + 3].isdigit():
                        check_num = line[char_num + 1] + line[char_num + 2] + line[char_num +3]
                    else:
                        check_num = line[char_num + 1] + line[char_num + 2]
                else:
                    check_num = line[char_num + 1]
                part_sum += int(check_num)
                #print(f"Right part number: {check_num}")
                number_of_gears += 1
                print(f"Right gear found: {check_num}")
                print(f"Number of gears: {number_of_gears}")
                if number_of_gears == 1:
                    gear1 = int(check_num)
                elif number_of_gears == 2:
                    gear2 = int(check_num)
                elif number_of_gears >= 3:
                    gear1 = 0
                    gear2 = 0
            

            #Check above
            if data[line_num - 1][char_num].isdigit():
                if data[line_num - 1][char_num - 1].isdigit():
                    if data[line_num - 1][char_num - 2].isdigit():
                        check_num = data[line_num - 1][char_num - 2] + data[line_num - 1][char_num - 1] + data[line_num - 1][char_num]
                    elif data[line_num - 1][char_num + 1].isdigit():
                        check_num = data[line_num - 1][char_num - 1] + data[line_num - 1][char_num] + data[line_num - 1][char_num + 1]
                    else:
                        check_num = data[line_num - 1][char_num - 1] + data[line_num - 1][char_num]
                elif data[line_num -1][char_num + 1].isdigit():
                    if data[line_num - 1][char_num + 2].isdigit():
                        check_num = data[line_num - 1][char_num] + data[line_num - 1][char_num + 1] + data[line_num - 1][char_num + 2]
                    else:
                        check_num = data[line_num - 1][char_num] + data[line_num - 1][char_num + 1]
                else:
                    check_num = data[line_num - 1][char_num]
                part_sum += int(check_num)
                #print(f"Top part number: {check_num}")
                number_of_gears += 1
                print(f"Upper gear found: {check_num}")
                print(f"Number of gears: {number_of_gears}")
                if number_of_gears == 1:
                    gear1 = int(check_num)
                elif number_of_gears == 2:
                    gear2 = int(check_num)
                elif number_of_gears >= 3:
                    gear1 = 0
                    gear2 = 0
            
            #Check upper-left diagonal
            elif data[line_num - 1][char_num - 1].isdigit():
                check_other_diagonal = True
                if data[line_num - 1][char_num - 2].isdigit():
                    if data[line_num - 1][char_num - 3].isdigit():
                        check_num = data[line_num - 1][char_num - 3] + data[line_num - 1][char_num - 2] + data[line_num - 1][char_num - 1]
                    else:
                        check_num = data[line_num - 1][char_num - 2] + data[line_num - 1][char_num - 1]
                else:
                    check_num = data[line_num - 1][char_num - 1]
                part_sum += int(check_num)
                #print(f"Diag Uppper Left part number: {check_num}")
                number_of_gears += 1
                print(f"Upper-left gear found: {check_num}")
                print(f"Number of gears: {number_of_gears}")
                if number_of_gears == 1:
                    gear1 = int(check_num)
                elif number_of_gears == 2:
                    gear2 = int(check_num)
                elif number_of_gears >= 3:
                    gear1 = 0
                    gear2 = 0
            
            #Check upper-right diagonal
            elif data[line_num - 1][char_num + 1].isdigit():
                if data[line_num - 1][char_num + 2].isdigit():
                    if data[line_num - 1][char_num + 3].isdigit():
                        check_num = data[line_num - 1][char_num + 1] + data[line_num - 1][char_num + 2] + data[line_num - 1][char_num + 3]
                    else:
                        check_num = data[line_num - 1][char_num + 1] + data[line_num - 1][char_num + 2]
                else:
                    check_num = data[line_num - 1][char_num + 1]
                part_sum += int(check_num)
                #print(f"Diag Upper Right part number: {check_num}")
                number_of_gears += 1
                print(f"Upper-right gear found: {check_num}")
                print(f"Number of gears: {number_of_gears}")
                if number_of_gears == 1:
                    gear1 = int(check_num)
                elif number_of_gears == 2:
                    gear2 = int(check_num)
                elif number_of_gears >= 3:
                    gear1 = 0
                    gear2 = 0
            
            if check_other_diagonal == True:
                if data[line_num - 1][char_num + 1].isdigit():
                    if data[line_num - 1][char_num + 2].isdigit():
                        if data[line_num - 1][char_num + 3].isdigit():
                            check_num = data[line_num - 1][char_num + 1] + data[line_num - 1][char_num + 2] + data[line_num - 1][char_num + 3]
                        else:
                            check_num = data[line_num - 1][char_num + 1] + data[line_num - 1][char_num + 2]
                    else:
                        check_num = data[line_num - 1][char_num + 1]
                    part_sum += int(check_num)
                    #print(f"Diag Upper Right part number: {check_num}")
                    number_of_gears += 1
                    print(f"Upper-right gear found: {check_num}")
                    print(f"Number of gears: {number_of_gears}")
                    if number_of_gears == 1:
                        gear1 = int(check_num)
                    elif number_of_gears == 2:
                        gear2 = int(check_num)
                    elif number_of_gears >= 3:
                        gear1 = 0
                        gear2 = 0
            
                check_other_diagonal = False


            #Check below
            if data[line_num + 1][char_num].isdigit():
                if data[line_num + 1][char_num - 1].isdigit():
                    if data[line_num + 1][char_num - 2].isdigit():
                        check_num = data[line_num + 1][char_num - 2] + data[line_num + 1][char_num - 1] + data[line_num + 1][char_num]
                    elif data[line_num + 1][char_num + 1].isdigit():
                        check_num = data[line_num + 1][char_num - 1] + data[line_num + 1][char_num] + data[line_num + 1][char_num + 1]
                    else:
                        check_num = data[line_num + 1][char_num - 1] + data[line_num + 1][char_num]
                elif data[line_num + 1][char_num + 1].isdigit():
                    if data[line_num + 1][char_num + 2].isdigit():
                        check_num = data[line_num + 1][char_num] + data[line_num + 1][char_num + 1] + data[line_num + 1][char_num + 2]
                    else:
                        check_num = data[line_num + 1][char_num] + data[line_num + 1][char_num + 1]
                else:
                    check_num = data[line_num + 1][char_num]
                part_sum += int(check_num)
                #print(f"Bottom part number: {check_num}")
                number_of_gears += 1
                print(f"Bottom gear found: {check_num}")
                print(f"Number of gears: {number_of_gears}")
                if number_of_gears == 1:
                    gear1 = int(check_num)
                elif number_of_gears == 2:
                    gear2 = int(check_num)
                elif number_of_gears >= 3:
                    gear1 = 0
                    gear2 = 0
            
            #Check lower-left diagonal
            elif data[line_num + 1][char_num - 1].isdigit():
                check_other_diagonal = True
                if data[line_num + 1][char_num - 2].isdigit():
                    if data[line_num + 1][char_num - 3].isdigit():
                        check_num = data[line_num + 1][char_num - 3] + data[line_num + 1][char_num - 2] + data[line_num + 1][char_num - 1]
                    else:
                        check_num = data[line_num + 1][char_num - 2] + data[line_num + 1][char_num - 1]
                else:
                    check_num = data[line_num + 1][char_num - 1]
                part_sum += int(check_num)
                #print(f"Diag Lower Left part number: {check_num}")
                print(f"Lower-left gear found: {check_num}")
                print(f"Number of gears: {number_of_gears}")
                number_of_gears += 1
                if number_of_gears == 1:
                    gear1 = int(check_num)
                elif number_of_gears == 2:
                    gear2 = int(check_num)
                elif number_of_gears >= 3:
                    gear1 = 0
                    gear2 = 0
            
            #Check lower-right diagonal
            elif data[line_num + 1][char_num + 1].isdigit():
                if data[line_num + 1][char_num + 2].isdigit():
                    if data[line_num + 1][char_num + 3].isdigit():
                        check_num = data[line_num + 1][char_num + 1] + data[line_num + 1][char_num + 2] + data[line_num + 1][char_num + 3]
                    else:
                        check_num = data[line_num + 1][char_num + 1] + data[line_num + 1][char_num + 2]
                else:
                    check_num = data[line_num + 1][char_num + 1]
                part_sum += int(check_num)
                #print(f"Diag Lower Right part number: {check_num}")
                print(f"Lower-right gear found: {check_num}")
                print(f"Number of gears: {number_of_gears}")
                number_of_gears += 1
                if number_of_gears == 1:
                    gear1 = int(check_num)
                elif number_of_gears == 2:
                    gear2 = int(check_num)
                elif number_of_gears >= 3:
                    gear1 = 0
                    gear2 = 0
            
            if check_other_diagonal == True:
                if data[line_num + 1][char_num + 1].isdigit():
                    if data[line_num + 1][char_num + 2].isdigit():
                        if data[line_num + 1][char_num + 3].isdigit():
                            check_num = data[line_num + 1][char_num + 1] + data[line_num + 1][char_num + 2] + data[line_num + 1][char_num + 3]
                        else:
                            check_num = data[line_num + 1][char_num + 1] + data[line_num + 1][char_num + 2]
                    else:
                        check_num = data[line_num + 1][char_num + 1]
                    part_sum += int(check_num)
                    #print(f"Diag Lower Right part number: {check_num}")
                    print(f"Lower-right gear found: {check_num}")
                    print(f"Number of gears: {number_of_gears}")
                    number_of_gears += 1
                    if number_of_gears == 1:
                        gear1 = int(check_num)
                    elif number_of_gears == 2:
                        gear2 = int(check_num)
                    elif number_of_gears >= 3:
                        gear1 = 0
                        gear2 = 0
            
                check_other_diagonal = False


            #print(regex_pattern.search(char))
            #print(check_num)
        char_num += 1
        #print(char_num)
        gear_ratio = gear1 * gear2
        gear_sum += gear_ratio
        print(f"Number of gears: {number_of_gears}")
        print(f"Gear 1: {gear1}, Gear 2: {gear2}, Gear Ratio: {gear_ratio}")
        print(f"The gear ratio sum is: {gear_sum}")
        number_of_gears = 0
        gear1 = 0
        gear2 = 0
    line_num += 1
    #print(f"Sum of Part Numbers: {part_sum}")

    
