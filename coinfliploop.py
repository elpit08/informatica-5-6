import random
def main():
    coin = ["heads","tails"]
    attempts = 3
    while attempts > 0:
        flip = random.choice(coin)
        guess = input("Heads or tails? ").strip().lower()

        print(f"The coin landed on {flip}")

        if guess == flip:
            print("You win!!")
            break
        else:
            print("You loose")
            attempts -= 1
            print(f"attempts left: {attempts}")

if __name__=="__main__":
    main()
