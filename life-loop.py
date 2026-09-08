import random

def main():

    restaurants= ["little ceasar","House","Fogueria","La sierra","Venezia","sushi box","Pon pon","Wok chicken","Dragon express","kung fu","Sirloncito","tacos rosas","Piporros","Carnitas michoacanas","Bronco tacos","Wendys","Rodeo","Erick burguer","Las Palmas","Miramar","Pollo feliz","KFC","Chicken country","fire food","Habanero wings","Pollo rostizado","hot dog","Bandidos","Munchfries","Subway","Pompeii"]

    #5 pizza, 5 asians, 5 mexican, 3 hamburguer, 2 mariscos, 6 pollo, 5 otros
    option = input("Choice a mode: Random or delimited: ").strip().lower()
    anwser = ""
    if option == 'random':
        print("I will chose a random restaurant")
        print("Write 'ok' to select the restaurant")
        while anwser != 'ok':
            print(random.choice(restaurants))
            anwser = input("Is the choice okey? ").lower().strip()

    elif option == 'delimited':
        print("Say what restaurant, you dont want to go to")
        print("Write 'ok' to select the restaurant")

        print("Select a type: 1)pizza     2)asian \n 3)mexican       4)hamburger\n 5)mariscos     6)pollo\n 7)otro")
        restaurant_type = input("Selection: ").lower().strip()
        while anwser != 'ok':
            if restaurant_type == 'pizza':
                pizza = random.randint(0,4)
                print(restaurants[pizza])
                anwser = input("Is the choice okey? ")

            elif restaurant_type == 'asian':
                asian = random.randint(5,9)
                print(restaurants[asian])
                anwser = input("Is the choice okey? ")

            elif restaurant_type == 'mexican':
                mexican = random.randint(10,14)
                print(restaurants[mexican])
                anwser = input("Is the choice okey? ")

            elif restaurant_type == 'hamburger':
                hamburger = random.randint(15,17)
                print(restaurants[hamburger])
                anwser = input("Is the choice okey? ")

            elif restaurant_type == 'mariscos':
                mariscos = random.randint(18,19)
                print(restaurants[mariscos])
                anwser = input("Is the choice okey? ")

            elif restaurant_type == 'pollo':
                pollo = random.randint(20,25)
                print(restaurants[pollo])
                anwser = input("Is the choice okey? ")

            elif restaurant_type == 'otro':
                otro = random.randint(26,30)
                print(restaurants[otro])
                anwser = input("Is the choice okey? ")

            else:
                print("Selection not valid")
                break

    else:
        print("Select a valid mode")


if __name__=="__main__":
    main()
