def main():
    table = int(input("Enter a number (1-10) "))
    exit = str(table).lower().strip()
    while exit != 'exit':
        for _ in range(1,11):
            print(f"{_} times {table} is {_ * table}")

        table = int(input("Enter a number (1-10) "))
        exit = str(table).lower().strip()

if __name__=="__main__":
    main()
