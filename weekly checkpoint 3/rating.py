def main():

    print("Tacos y Gorditas dona goya ")
    review = float(input("What is your rating: "))



    if 5.1 > review > 4.4:
        print("Perfection")

    elif 4.5 > review > 3.9:
        print("Excellent")

    elif 4 > review > 2.9:
        print("Good")

    elif 3 > review > 1.9:
        print("Fair")

    elif 2 > review > 0:
        print("Poor")

    else:
        print("value not possible")

if __name__=="__main__":
    main()
