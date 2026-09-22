def main():

    mario = ["Princess Peach","Mario","Luigi","Daisy","Yoshi","Toad","Bowser","Toadette","Waluigi","Wario"]


    for _ in range(1,len(mario)):
        print(f"""    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {mario[_]},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {mario[0]}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+  """)






if __name__=="__main__":
    main()
