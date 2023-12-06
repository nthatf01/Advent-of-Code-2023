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

seeds = "3127166940 109160474 3265086325 86449584 1581539098 205205726 3646327835 184743451 2671979893 17148151 305618297 40401857 2462071712 203075200 358806266 131147346 1802185716 538526744 635790399 705979250".split(" ")

seed_to_soil = read_csv_file('day_5_seed_to_soil_map.csv')
soil_to_fertilizer = read_csv_file('day_5_soil_to_fertilizer_map.csv')
fertilizer_to_water = read_csv_file('day_5_fertilizer_to_water_map.csv')
water_to_light = read_csv_file('day_5_water_to_light_map.csv')
light_to_temperature = read_csv_file('day_5_light_to_temperature_map.csv')
temperature_to_humidity = read_csv_file('day_5_temperature_to_humidity_map.csv')
humidity_to_location = read_csv_file('day_5_humidity_to_location_map.csv')

#print(seeds)

#Day 5 Part 1

lowest_location = 999999999999999
locations = []

for seed in seeds:
    soil = -1
    fertilizer = -1
    water = -1
    light = -1
    temperature = -1
    humidity = -1
    location = -1
    #print(seed)

    #Find Destination Soil
    for line in seed_to_soil:
        s2s_nums = line.split(" ")
        #print(s2s_nums)
        if int(s2s_nums[1]) <= int(seed) <= int(s2s_nums[1]) + int(s2s_nums[2]):
            soil = (int(seed) - int(s2s_nums[1])) + int(s2s_nums[2])
            print(f"FOUND: Source Seed: {int(s2s_nums[1])}, Seed: {int(seed)}, Range: {int(s2s_nums[2])}, Destination Soil: {soil}")
    if soil == -1:
        soil = int(seed)
        print(f"NOT FOUND: Source Seed: {int(s2s_nums[1])}, Seed: {int(seed)}, Range: {int(s2s_nums[2])}, Destination Soil: {soil}")
    print(f"SOIL CHECK: {soil}")
    
    #Find Destination Fertilizer
    for line in soil_to_fertilizer:
        s2f_nums = line.split(" ")
        #print(s2f_nums)
        if int(s2f_nums[1]) <= int(soil) <= int(s2f_nums[1]) + int(s2f_nums[2]):
            fertilizer = (int(soil) - int(s2f_nums[1])) + int(s2f_nums[0])
            print(f"FOUND: Source Soil: {int(s2f_nums[1])}, Seed: {int(seed)}, Range: {int(s2f_nums[2])}, Destination Fertilizer: {fertilizer}")
    if fertilizer == -1:
        fertilizer = int(soil)
        print(f"NOT FOUND: Source Soil: {int(s2f_nums[1])}, Seed: {int(seed)}, Range: {int(s2f_nums[2])}, Destination Fertilizer: {fertilizer}")

    #Find Destination Water
    for line in fertilizer_to_water:
        f2w_nums = line.split(" ")
        if int(f2w_nums[1]) <= int(fertilizer) <= int(f2w_nums[1]) + int(f2w_nums[2]):
            water = (int(fertilizer) - int(f2w_nums[1])) + int(f2w_nums[0])
            print(f"FOUND: Source Fertilizer: {int(f2w_nums[1])}, Seed: {int(seed)}, Range: {int(f2w_nums[2])}, Destination Water: {water}")
    if water == -1:
        water = int(fertilizer)
        print(f"NOT FOUND: Source Fertilizer: {int(f2w_nums[1])}, Seed: {int(seed)}, Range: {int(f2w_nums[2])}, Destination Water: {water}")

    #Find Destination Light
    for line in water_to_light:
        w2l_nums = line.split(" ")
        if int(w2l_nums[1]) <= int(water) <= int(w2l_nums[1]) + int(w2l_nums[2]):
            light = (int(water) - int(w2l_nums[1])) + int(w2l_nums[0])
            print(f"FOUND: Source Water: {int(w2l_nums[1])}, Seed: {int(seed)}, Range: {int(w2l_nums[2])}, Destination Light: {light}")
    if light == -1:
        light = int(water)
        print(f"NOT FOUND: Source Water: {int(w2l_nums[1])}, Seed: {int(seed)}, Range: {int(w2l_nums[2])}, Destination Light: {light}")

    #Find Destination Temperature
    for line in light_to_temperature:
        l2t_nums = line.split(" ")
        if int(l2t_nums[1]) <= int(light) <= int(l2t_nums[1]) + int(l2t_nums[2]):
            temperature = (int(light) - int(l2t_nums[1])) + int(l2t_nums[0])
            print(f"FOUND: Source Light: {int(l2t_nums[1])}, Seed: {int(seed)}, Range: {int(l2t_nums[2])}, Destination Temperature: {temperature}")
    if temperature == -1:
        temperature = int(light)
        print(f"NOT FOUND: Source Light: {int(l2t_nums[1])}, Seed: {int(seed)}, Range: {int(l2t_nums[2])}, Destination Temperature: {temperature}")

    #Find Destination Humidity
    for line in temperature_to_humidity:
        t2h_nums = line.split(" ")
        if int(t2h_nums[1]) <= int(temperature) <= int(t2h_nums[1]) + int(t2h_nums[2]):
            humidity = (int(temperature) - int(t2h_nums[1])) + int(t2h_nums[0])
            print(f"FOUND: Source Temperature: {int(t2h_nums[1])}, Seed: {int(seed)}, Range: {int(t2h_nums[2])}, Destination Humidity: {humidity}")
    if humidity == -1:
        humidity = int(temperature)
        print(f"NOT FOUND: Source Temperature: {int(t2h_nums[1])}, Seed: {int(seed)}, Range: {int(t2h_nums[2])}, Destination Humidity: {humidity}")

    #Find Destination Location
    for line in humidity_to_location:
        h2t_nums = line.split(" ")
        if int(h2t_nums[1]) <= int(humidity) <= int(h2t_nums[1]) + int(h2t_nums[2]):
            location = (int(humidity) - int(h2t_nums[1])) + int(h2t_nums[0])
            print(f"FOUND: Source Humidity: {int(h2t_nums[1])}, Seed: {int(seed)}, Range: {int(h2t_nums[2])}, Destination Location: {location}")
    if location == -1:
        location = int(humidity)
        print(f"NOT FOUND: Source Humidity: {int(h2t_nums[1])}, Seed: {int(seed)}, Range: {int(h2t_nums[2])}, Destination Location: {location}")

    locations.append(location)

    if location < lowest_location:
        lowest_location = location
    
    print(" ")

print(f"Lowest found location: {lowest_location}")
print(locations)




