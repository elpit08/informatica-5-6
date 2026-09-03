import random
def main():

    user = input("What is your name? ")
    difficulty = input("Select the difficulty: Easy, Medium, Hard, Satan: ").strip().lower()
    attempts = 0
    print(f"Well, {user}, Guess the number Im thinking" )

    if difficulty == 'easy':
        number = random.randint(1,20)
        while attempts < 7:
            guess = int(input("Is a number between 1-20: "))

            if guess > number:
                print("Number too high")

            elif guess < number:
                print("Number too low")

            elif guess == number:
                print("You guessed my Number, YOU WON")
                print(f"Number of attempts: {attempts}")
                break
            else:
                print("Not a valid number")

            attempts += 1



    elif difficulty == 'medium':
        number = random.randint(1,100)
        while attempts < 7:
            guess = int(input("Is a number between 1-100: "))

            if guess > number:
                print("Number too high")

            elif guess < number:
                print("Number too low")

            elif guess == number:
                print("You guessed my Number, YOU WON")
                print(f"Number of attempts: {attempts}")
                break
            else:
                print("Not a valid number")

            attempts += 1

    elif difficulty == 'hard':
        number = random.randint(1,500)
        while attempts < 7:
            guess = int(input("Is a number between 1-500: "))

            if guess > number:
                print("Number too high")

            elif guess < number:
                print("Number too low")

            elif guess == number:
                print("You guessed my Number, YOU WON")
                print(f"Number of attempts: {attempts}")
                break
            else:
                print("Not a valid number")

            attempts += 1

    elif difficulty == 'satan':
        number = random.randint(1,1000000)
        while attempts < 11:
            guess = int(input("Is a number between 1-1,000,000: "))

            if guess > number:
                print("Number too high")

            elif guess < number:
                print("Number too low")

            elif guess == number:
                print("You guessed my Number, YOU WON")
                print(f"Number of attempts: {attempts}")
                break
            else:
                print("Not a valid number")

            attempts += 1
    else:

        print("select a valid difficulty ")






if __name__=="__main__":
    main()
