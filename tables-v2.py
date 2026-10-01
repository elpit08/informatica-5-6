def main():
    he_wrote_integer1 = True
    he_wrote_integer2 = True
    print("Welcome to the times table quiz")

    while he_wrote_integer1:
        try:
            test_number = int(input("Enter the times table you would like to be tested on: "))
            he_wrote_integer1 = False
        except ValueError:
            print("Please select a number" )

    while he_wrote_integer2:
        try:
            max_value = int(input("Enter the maximun value for the times table: "))
            he_wrote_integer2 = False
        except ValueError:
            print("Please select a number")

    print(f"You will be tested on the {test_number} table")
    grade = 0

    for _ in range(1, max_value + 1):

        anwser = _ * test_number
        try:
            user_anwser = int(input(f"{_} times {test_number} is "))


            if user_anwser == anwser:
                grade += 1
                print("correct")

            else:
                print("Incorrect")

        except ValueError:
            print("Anwser with a number")

    print(f"You got {grade} out of {max_value}")
    print(round(grade / max_value * 100, 2), "%")





if __name__=="__main__":
    main()
