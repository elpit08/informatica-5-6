def main():
    table = input("Enter a number (1-10) ")
    while table != 'exit':
        number = int(table)
        max_value = int(input("Enter a maximum value of the times table: "))
        for _ in range(1,max_value + 1):

            print(f"{_} times {number} is {_ * number}")


        table = input("Enter a number (1-10) ").lower().strip()



if __name__=="__main__":
    main()
