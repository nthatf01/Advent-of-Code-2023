import csv
import time
import sys

startTime = time.perf_counter()

def read_csv_file(file_path):
    data_list = []

    try:
        with open(file_path, mode = 'r', encoding = 'utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Skip the header row if it exists
            # header = next(csv_reader, None)

            for row in csv_reader:
                data_list.append(str(row)[2:-2].split(" "))
                
        return data_list

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

csv_file_path = 'day_7_input.csv'
data = read_csv_file(csv_file_path)

card_values = {"A":13,
               "K":12,
               "Q":11,
               "T":10,
               "9":9,
               "8":8,
               "7":7,
               "6":6,
               "5":5,
               "4":4,
               "3":3,
               "2":2,
               "J":1}

signatures = []

for hand, bid in data:
    hand_signature = 0
    unique_cards = set(hand)
    num_jokers = hand.count("J")
    match len(unique_cards):
        case 1:
            #Five of a kind
            hand_signature = 70000000000
        case 2:
            largest_num = 0
            for card in unique_cards:
                if hand.count(card) > largest_num:
                    largest_num = hand.count(card)
            if largest_num == 4:
                if num_jokers == 1 or num_jokers == 4:
                    #Five of a kind (four + one Joker, or one + four Jokers)
                    hand_signature = 70000000000
                else:
                    #Four of a kind
                    hand_signature = 60000000000
            else:
                if num_jokers == 3 or num_jokers == 2:
                    #Five of a kind (two + three Jokers, or three + two Jokers)
                    hand_signature = 70000000000
                elif num_jokers == 1:
                    #Four of a kind (three + one Joker)
                    hand_signature = 60000000000
                else:
                    #Full house
                    hand_signature = 50000000000
        case 3:
            largest_num = 0
            for card in unique_cards:
                 if hand.count(card) > largest_num:
                     largest_num = hand.count(card)
            if largest_num == 3:
                if num_jokers == 3 or num_jokers == 1:
                    #Four of a kind (one + three Jokers, or three + one Joker)
                    hand_signature = 60000000000
                else:
                    #Three of a kind
                    hand_signature = 40000000000
            else:
                if num_jokers == 2:
                    #Four of a kind (two + two Jokers)
                    hand_signature = 60000000000
                elif num_jokers == 1:
                    #Full house (two + one Joker)
                    hand_signature = 50000000000
                else:
                    #Two pair
                    hand_signature = 30000000000
        case 4:
            if num_jokers == 2 or num_jokers == 1:
                #Three of a kind (one + two Jokers, or two + one Joker)
                hand_signature = 40000000000
            else:
                #One pair
                hand_signature = 20000000000
        case 5:
            if num_jokers == 1:
                #One pair (one + one Joker)
                hand_signature = 20000000000
            else:
                #High card
                hand_signature = 10000000000

    hand_signature += (card_values[hand[0]] * 100000000) + (card_values[hand[1]] * 1000000) + (card_values[hand[2]] * 10000) + (card_values[hand[3]] * 100) + (card_values[hand[4]] * 1)
    #if num_jokers > 0:
        #print(f"Hand: {hand}; Bid: {bid}; Signature: {hand_signature}")
    signatures.append((str(hand_signature) + " " + str(bid)).split(" "))

signatures.sort()
hand_rank = 0
total_winnings = 0

for hand_signature, bid in signatures:
    hand_rank += 1
    total_winnings += int(bid) * int(hand_rank)

print(f"Total winnings: {total_winnings}")

print(f"Time elapsed: {(time.perf_counter() - startTime)}s", file=sys.stderr)
