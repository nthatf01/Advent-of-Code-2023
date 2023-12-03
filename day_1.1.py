import csv
import string

def read_csv_file(file_path):
    data_list = []

    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Skip the header row if it exists
            # header = next(csv_reader, None)

            for row in csv_reader:
                data_list.append(str(row))

        return data_list

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

csv_file_path = 'day_1.1_input.csv'
data = read_csv_file(csv_file_path)

calibration_sum = 0
line_count = 0

for line in data:
    line_count = line_count + 1
    calibration_value = 0
    print(line)
    for char in line:
        if char.isdigit():
            calibration_value = int(char) * 10
            break
    for char in line[ : :-1]:
        if char.isdigit():
            calibration_value = calibration_value + int(char)
            print(calibration_value)
            break
    calibration_sum = calibration_sum + calibration_value
    print(calibration_sum)

print(calibration_sum)
print(line_count)
