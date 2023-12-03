import csv

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

csv_file_path = 'day_2_input.csv'
data = read_csv_file(csv_file_path)

#Day 2
#Part 1

game_number = 0
pull_number = 0
check_red = 12
check_blue = 14
check_green = 13
game_sum = 0

for game in data:
    pull_number = 0
    game_number += 1
    max_red = 0
    max_blue = 0
    max_green = 0
    #print(f"Game #: {game_number}")
    colon_position = game.find(":")
    game = game[(colon_position + 2):]
    pulls = game.split(";")
    for pull in pulls:
        pull_number += 1
        #print(f"Pull #: {pull_number}")
        colors = pull.split(",")
        for color in colors:
            #print(color)
            if "red" in color:
                space_position = color.find("r")
                number_color = int(color[:space_position].replace("'", "").strip())
                if number_color > max_red:
                    max_red = number_color
            if "blue" in color:
                space_position = color.find("b")
                number_color = int(color[:space_position].replace("'", "").strip())
                if number_color > max_blue:
                    max_blue = number_color
            if "green" in color:
                space_position = color.find("g")
                number_color = int(color[:space_position].replace("'", "").strip())
                if number_color > max_green:
                    max_green = number_color

    if max_red <= check_red and max_blue <= check_blue and max_green <= check_green:
        game_sum += game_number
            
    print(f"Max Red: {max_red}, Max Blue: {max_blue}, Max Green: {max_green}")
    print(game_sum)
