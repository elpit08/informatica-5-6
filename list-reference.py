def main():
    x = len("hello")


    print(x)


    password = [1, 2, 3, 4, 5, 6, 7, 8]

    xx = ["a", "b", "c", "d"]

    xx.append("e")


    print(len(xx))

    print(password)




    change = input(" ")

    if change == "y":
    password[1]= 4
    password[0] = 2
    password[7] = 1
    password[6] = 9
    password[5] = 10
    password.insert(0,99)
    password.insert(2,42)
    print(password)


    tacos = ["Ojo","tripa","asada","pastor","mixtos"]
    print(tacos.pop(2))
    print(tacos)
    print(tacos.remove("Ojo"))
    print(tacos)

    tacos.append("gobernador")
    print(tacos)

    print(max(xx))
    print(min(xx))
    print(sum(xx))
    xx.sort()
    print(xx)



if __name__=="__main__"
    main()
