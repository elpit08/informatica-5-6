def main():
    eq = input("Input equation: ")
    equation = eq.split( )
    number1 = float(equation[0])
    operation = equation[1]
    number2 = float(equation[2])

    if operation == '+':
        print(number1 + number2)

    elif operation == '-':
        print(number1 - number2)

    elif operation == '*':
        print(number1 * number2)

    elif operation == '/':
        print(number1 / number2)


if __name__=="__main__":
    main()
