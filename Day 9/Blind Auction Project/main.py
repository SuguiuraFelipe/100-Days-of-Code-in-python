import art
dictionary = {}

def start():
    print(art.logo)
    user = input("What is your name?\n")
    price = int(input("What's your bid?: €\n"))
    dictionary[user] = price
    restart()

def restart():
    while True:
        new_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if new_bid == "yes":
            print("\n" * 20)
            new_user = input("What is your name?\n")
            new_price = int(input("What's your bid?\n"))
            dictionary[new_user] = new_price
        elif new_bid == "no":
            max_key = None
            max_value = float("-inf")
            for key, value in dictionary.items():
                if value > max_value:
                    max_value = value
                    max_key = key
            print(f"The winner is {max_key} with a bid of {max_value}")
            break
        else:
            print("You typed something wrong, try again.")

start()
