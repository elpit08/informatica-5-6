def binary_to_decimal(a):

    final = ""
    decimal = 0
    list_binary = []

    for _ in a:
        list_binary.append(_)
    list_binary.reverse()

    for _ in range(len(list_binary)):

        if list_binary[_] == '1':
            decimal = decimal + 2**(_)

        elif list_binary[_] != '0':
            final = 'Not a valid character'


    if final == 'Not a valid character':
        print(final)
    else:
        print(f"decimal number: {decimal}")


def main():
    print("Binary to decimal converter\n")
    print("""The purpuse of this program is to convert binary numbers
into normal numbers(decimal numbers)
""")
    repeat = True
    while repeat:
        user_convertion = input("Enter a binary number(only 0 or 1): ")
        list_binary = []

        for _ in user_convertion:
                list_binary.append(_)

        for _ in range(len(list_binary)):
            if list_binary[_] == '1' or list_binary[_] == '0':
                repeat = False



    binary_to_decimal(user_convertion)



if __name__=="__main__":
    main()
