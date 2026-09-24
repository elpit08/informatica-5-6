def main():
    table = input("Enter a number (1-10) ")
    #number = int(table)
    while table != 'exit':
        number = int(table)
        for _ in range(1,11):

            print(f"{_} times {number} is {_ * number}")

        table = input("Enter a number (1-10) ")


if __name__=="__main__":
    main()
