def main():
    width = int(input("What is the width of the rectangle? \n"))
    o = "O"
    area = width*5
    perimeter = 2*width+10
    z = width*o
    diagonal = (width**2+25)**(1/2)
    print(" Rectangle: ")
    print(f" {z}\n {z}\n {z}\n {z}\n {z}\n")
    print(f"perimeter:{perimeter}")
    print(f"area:{area}")
    print(f"diagonal:{diagonal}")



if __name__=="__main__":
    main()
