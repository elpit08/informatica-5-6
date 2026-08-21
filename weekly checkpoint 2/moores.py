def main():

    transistors = 17800000000
    year =int(input("How many years into the future? "))

    year /= 2
    year = 2 ** year
    transistors *= year
    print(f"In the future there will be: {transistors} transistors")



if __name__=="__main__":
    main()
