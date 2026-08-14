def main():
    name = input("what is your name?").strip().title()
    color = input("Tell me a color:").strip()
    adjetive = input("Tell me an adjetive:").strip()
    goal = input("What is a goal you have:")

    print(f"Hello, {name}!", end="\n\n")
    print("This is your story:")

    print(f"When I was in the school I {adjetive} and didnt think to much about it \n",f"but when I looked at my {color} friend I remembered I wanted to {goal}")
    print(f"When I was in the school I {adjetive} and didnt think to much about it \n",f"but when I looked at my {color} friend I remembered I wanted to {goal}".upper())



    #planet = input("Planet:")
    #Separation
    #print("Hello", planet)
    #concatenation
    #print("Hello " +planet)
    #Formatted Strings
    #print(f"Hello {planet}")
    #Ending
    #print("Hello", end=" ")
    #print(planet)

if __name__ == "__main__":
    main()
