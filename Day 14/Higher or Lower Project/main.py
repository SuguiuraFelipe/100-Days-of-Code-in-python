import random
import art
import game_data

def play():
    score = 0
    while score >= 0:
        player1_idx, player2_idx = random.sample(range(len(game_data.data)), 2)

        player1 = game_data.data[player1_idx]
        name1 = player1['name']
        description1 = player1['description']
        country1 = player1['country']
        followers1 = player1['follower_count']

        player2 = game_data.data[player2_idx]
        name2 = player2['name']
        description2 = player2['description']
        country2 = player2['country']
        followers2 = player2['follower_count']

        print(art.logo)
        print(f"Compare A: {name1}, {description1}, {country1}")
        print(art.vs)
        print(f"Against B: {name2}, {description2}, {country2}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == 'a':
            if followers1 > followers2:
                score += 1
                print(20 * "\n")
                print(f"You're right! Current score: {score}")
            else:
                print(20 * "\n")
                print(f"Sorry, that's wrong. Final score: {score}")
                score -=1000
        elif answer == 'b':
            if followers2 > followers1:
                print(20 * "\n")
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(20 * "\n")
                print(f"Sorry, that's wrong. Final score: {score}")
                score -= 1000


play()