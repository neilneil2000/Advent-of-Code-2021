from bingo_card import BingoCard

def main():
    numbers, cards = read_input_file("DayFourInput")
    index = 0
    while True:
        next_number = int(numbers[index])
        for card in cards:
            card.check_new_number(next_number)
            if card.won:
                print("We have a winner!")
                sum = card.sum_remaining_values()
                break
        if card.won:
            break
        index += 1
    
    print("Last Number called: " + str(next_number))
    print("Sum of Remaining Values: " + str(sum))
    answer = next_number * sum
    print("Part 1 answer: " + str(answer))



def check_cards(number,cards):
    pass

def read_input_file(filename):
    f = open(filename,'r')
    line = f.readline()
    numbers = line.strip().split(",")
    cards = []
    for x in range(0,100):
        line = f.readline()
        new_card = read_bingo_card(f)
        cards.append(new_card)
    return numbers, cards

def read_bingo_card(file):
    card = BingoCard()
    for x in range(0,5):
        line = file.readline()
        line = line.strip().split(" ")
        while len(line) > 5:
            line.remove('')
        card.add_row(line)
    return card
        


if __name__ == '__main__':
    main()