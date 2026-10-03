def main ():
    not_val = True
    while not_val:

        try:
            guess = int(input("Enter a number between 1-10: "))
            if 0 < guess < 11:
                not_val = False
                print("Success")

            else:
                print("You Must enter a number 1-10")

        except ValueError:
            print("You Must enter a number 1-10")

    repeat = True
    while repeat:
        try:
            name = input("enter a name: ")
            print(f"Stored name: {name}")
            if name != "":
                repeat = False
        except ValueError:
            print("You must enter a number")


if __name__== "__main__":
    main()
