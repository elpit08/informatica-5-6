def main():

#is it a finite group? yes
    response = ""
    followup = ""

    while response != 'yes!':
        response = input("Are we there yet? ").lower().strip()

        if response == 'yes':
            followup = input("really? ").lower().strip()

        if followup == 'yes':
            break

    print("We are finally here")

if __name__=="__main__":
    main()
