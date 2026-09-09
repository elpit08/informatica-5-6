import random

def main():
    print("Notdualingo")
    difficulty = input("Select a difficulty: \n add ; subtract ; multiply \n").lower().strip()
    streak = 0


    if difficulty == 'add':
        while streak < 3:
            number1 = random.randint(10,99)
            number2 = random.randint(10,99)

            anwser = int(input(f"What is {number1} + {number2} ?"))

            if anwser == number1 + number2:
                print("Congratulations is Correct ")
                streak += 1
                print(f"Your streak is: {'🌟' * streak}")

            else:
                print("Incorrect \n try again")

    elif difficulty == 'subtract':
        while streak < 3:
            number1 = random.randint(10,99)
            number2 = random.randint(10,99)
            anwser = int(input(f"What is {number1} - {number2} ?"))

            if anwser == number1 - number2:
                print("Congratulations is Correct ")
                streak += 1
                print(f"Your streak is: {'🌟' * streak}")

            else:
                print("Incorrect \n try again")

    elif difficulty == 'multiply':
        while streak < 3:
            number1 = random.randint(10,99)
            number2 = random.randint(10,99)
            anwser = int(input(f"What is {number1} * {number2} ?"))

            if anwser == number1 * number2:
                print("Congratulations is Correct ")
                streak += 1
                print(f"Your streak is: {'🌟' * streak}")

            else:
                print("Incorrect \n try again")

    else:
        print("Select a valid difficulty")

if __name__=="__main__":
    main()
