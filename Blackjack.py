import random

def blackjack():
    card_list = ["1",
                 "2",
                 "3",
                 "4",
                 "5",
                 "6",
                 "7",
                 "8",
                 "9",
                 "10",
                 #jack:
                 "10",
                 #queen:
                 "10",
                 #king:
                 "10"
                 ]
    card_list = card_list * 4
    random_card = random.randint(0, 51)
    card1 = card_list[random.randint(0, 51)]
    card2 = card_list[random.randint(0, 51 - 1)]
    card3 = card_list[random.randint(0, 51 - 2)]
    hand = card1 + "  " + card2
    
    print("Welcome to Python Blackjack.")
    print("The Rules:")
    print("""The goal is to get the sum of your cards as close
          to 21 without going over. All face cards are worth 10 
          and Aces are 1. You receive 2 cards to start. You can
          choose to 'hit' to receive a third card. If you want to
          trade out the third card again, choose 'hit' for your
          next move. If you want to stop cycling your third card,
          choose 'stand'. Good luck!""")
    print(hand)

    if len(hand) < 3:
        i = 0
        for cards in hand:
            sum = hand[i]
            sum = int(card1 + card2)
            i += 1
    else:
        i = 0
        for cards in hand:
            sum = hand[i]
            sum = int(card1) + int(card2) + int(card3)
            i += 1
    
    print(sum)
    while sum < 21:
        print("\n")
        msg = "hit or stand? "
        move = input(msg)
        if move == "hit":
            
            hand = card1 + " " + card2 + " " + card3
            print(hand)
        if move == "stand":
            if sum == 21:
                print("You got 21, you win!")
            if sum > 17:
                print("That's a pretty good hand")
            if sum < 17:
                print("Better luck next time, the dealer has won")
            break
        else:
            "Please enter 'hit' or 'stand'"
    else:
        print("You're over 21, you bust!")

blackjack()
          

