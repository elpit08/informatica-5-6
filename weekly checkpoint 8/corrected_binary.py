def binary_to_decimal(a):
    dnumber = 0
    for bit in a:
        dnumber = (dnumber * 2) + int(bit)
    print(dnumber)

def main():
    print("Welcome!")

    valid_bits = ['1','0']
    while True:
        user_binary = input("Enter a binary number: ")
        valid_char = 0
        for _ in user_binary:
            if _ in valid_bits:
                valid_char +=1
        if valid_char == len(user_binary):
            break
        else:
            print("Try again")

    binary_to_decimal(user_binary)

if __name__=="__main__":
    main()
