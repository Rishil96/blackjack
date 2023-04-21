# Black Jack
import random
from art import logo

# Cards
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
BLACKJACK = 21


# Get card
def get_card():
    return random.choice(cards)


# Check if game is over
def is_game_over(hand: list, total: int) -> bool:
    if total > BLACKJACK:
        if 11 in hand:
            for index in range(0, len(hand)):
                if hand[index] == 11:
                    hand[index] = 1
                    break
            return False

        else:
            return True
    else:
        return False


# Get winner
def get_winner(player: int, dealer: int):
    if player > dealer:
        print("Player Wins.")
        print(f"Final Score:\nPlayer: {player}\nDealer: {dealer}")
    elif dealer > player:
        print("Dealer Wins.")
        print(f"Final Score:\nPlayer: {player}\nDealer: {dealer}")
    else:
        print("It is a draw!")


# Game logic
def play():
    print(logo)

    player_hand = []
    dealer_hand = []

    for _ in range(0, 2):
        player_hand.append(get_card())
        dealer_hand.append(get_card())

    player_total = sum(player_hand)
    dealer_total = sum(dealer_hand)

    print("It is your turn.")
    is_playing = True
    player_lost = False

    while is_playing:
        print(f"\nYour Hand: {player_hand}")
        print(f"Dealer's First Card: {dealer_hand[0]}")
        choice = input("\nHit or Stand? (H/S): ").lower()

        if choice.startswith("h"):
            player_hand.append(get_card())
            player_total = sum(player_hand)
            if is_game_over(player_hand, player_total):
                player_lost = True
                is_playing = False
                print("\nBUSTED! You lose.")
                print(f"Your Final Hand: {player_hand}")

        elif choice.startswith("s"):
            print(f"\nYour Final Hand: {player_hand}")
            print(f"Your Total Score: {player_total}")
            is_playing = False

        else:
            print("\nInvalid Choice. Try again.")
            continue

    if not player_lost:
        print("It is dealer's turn.")
        while dealer_total < 17:
            dealer_hand.append(get_card())
            dealer_total = sum(dealer_hand)

        if dealer_total > BLACKJACK:
            print("Dealer BUSTED! You win.")
        else:
            get_winner(player_total, dealer_total)

    play_again = input("\nDo you want to play again? Y|N: ").lower()

    if play_again.startswith("y"):
        play()
    else:
        print("\nThanks for playing BlackJack.")


if __name__ == "__main__":
    play()
