
import random

def main():
    print("Coin flip the game")
    print("1 = HEADS,   2 = Tails")
    guess = input("Heads or Tails? ").lower().strip()
    coin_flip = random.randint(1,2)

    if guess == 'heads':
        print(f"You guessed {guess}, the coin was {coin_flip}")
        if coin_flip == 1:
            print("You won!!")
        else:
            print("You loose")

    elif guess == 'tails':
        print(f"You guessed {guess}, the coin was {coin_flip}")
        if coin_flip == 2:
            print("You won!!")
        else:
            print("You loose")

    else:
        print("Option not valid")



if __name__=="__main__":
    main()
