def highest(a,b):
    if a > b:
        print(f"The highest entered number is {a}")
    elif b > a:
        print(f"The highest entered number is {b}")
    elif b == a:
        print("Both numbers are the same")
    else:
        print("Not a valid number")

def lowest(a,b):
    if a > b:
        print(f"The lowest entered number is {b}")
    elif b > a:
        print(f"The lowest entered number is {a}")
    elif b == a:
        print("Both numbers are the same")
    else:
        print("Not a valid number")
def main():

    print("Select the mode")
    mode = input("Highest or lowest: ").lower().strip()

    if mode == 'lowest':
        num1 = int(input("Write your first number: "))
        num2 = int(input("Write the second number: "))
        lowest(num1,num2)

    elif mode == 'highest':
        num1 = int(input("Write your first number: "))
        num2 = int(input("Write the second number: "))
        highest(num1,num2)



if __name__=="__main__":
    main()
