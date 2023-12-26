import csv
import time
import sys
import math
from itertools import product
from PIL import Image

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

def create_bitmap(coordinates):
    #Create a blank white image
    img = Image.new('RGB', (1000, 1000), 'white')

    # Draw pixels at specified coordinates
    for coordinate in coordinates:
        y, x = coordinate
        img.putpixel((x, y), (0, 0, 0))  # Set pixel color to black

    # Save the image as a BMP file
    img.save("day_18_image.bmp")

csv_file_path = 'day_18_input.csv'
data = read_csv_file(csv_file_path)
csv_file_path = 'day_18_test_input.csv'
test_data = read_csv_file(csv_file_path)

#lagoon_data = test_data
lagoon_data = data


directions = {
    "U": {
        "X": (0),
        "Y": (-1),
        "U": (0),
        "D": (0),
        "L": (-1),
        "R": (1)
        },
    "D": {
        "X": (0),
        "Y": (1),
        "U": (0),
        "D": (0),
        "L": (1),
        "R": (-1)
        },
    "L": {
        "X": (-1),
        "Y": (0),
        "U": (1),
        "D": (-1),
        "L": (0),
        "R": (0),
        },
    "R": {
        "X": (1),
        "Y": (0),
        "U": (-1),
        "D": (1),
        "L": (0),
        "R": (0)
        }
    }

lagoon_border = {}
previous_direction = lagoon_data[0][0]
turns = 0
cursor = [500, 500]
pos = ""
img_coords = []

for direction, length, color in lagoon_data:
    #print(f"Direction: {direction}, Length: {length}, Color: {color}")

    for i in range(0, int(length)):
        #print(f"Current coordinates: {cursor[0]}, {cursor[1]}")
        img_coords.append(tuple([cursor[0], cursor[1]]))
        cursor[0] += directions[direction]["Y"]
        cursor[1] += directions[direction]["X"]

#print(img_coords)
create_bitmap(img_coords)


print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)





