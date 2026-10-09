def welcome():
    print("Welcome to Elburgesas")
    print("Heres the menu: ")
    menu = ['cheeseburguer','Fries','Soda','Ice cream','Cookie']
    for _ in menu:
        print(f"{menu.index(_) + 1}. {_}")

def get_item(a):
    if a == "cheeseburguer" or a == '1':
        print("Here is your 🍔")

    elif a == "fries" or a == '2':
        print("Here is your 🍟")

    elif a == "soda" or a == '3':
        print("Here is your 🥤")

    elif a == "ice cream" or a == '4':
        print("Here is your 🍦")

    elif a == "cookie" or a == '5':
        print("Here is your 🍪")

    else:
        print("not a valid option")



def main():
    welcome()
    user_selection = input("What item do you want? ").lower().strip()
    get_item(user_selection)


if __name__=="__main__":
    main()
