def main():
    spain = int(input("Spain goals: "))
    cabo_verde = int(input("Cabo verde goals: "))

    if spain > cabo_verde:
        print("Spain is the WINNER!!")

    elif cabo_verde > spain:
        print("Cabo verde is the WINNER !")

    else:
        print("Its a tie. ")

    print("gg")

if __name__=="__main__":
    main()
