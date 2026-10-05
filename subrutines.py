def average_value(a, b, c):
    average = (a + b + c)/3
    print(f"the average value is {average}")

def main():
    print("Calculate the average")
    num1 = float(input("What is the first value: "))
    num2 = float(input("What is the second value: "))
    num3 = float(input("What is the last value: "))

    average_value(num1,num2,num3)



    def calculate(a, b):
        anwser = a + b
        print(f"{a} + {b} = {anwser}")

    number1 = 10
    number2 = 15

    calculate(number1, number2)




if __name__=="__main__":
    main()
