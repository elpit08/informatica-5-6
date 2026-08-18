def main():

    brazil= float(input("How many reais do you have? "))
    colombia=float(input("How many pesos do you have? "))
    peru=float(input("How many soles do you have? "))

    ucolombia= colombia/3132.21
    ubrazil= brazil/5.22
    uperu= peru/3.37
    total_USD=ucolombia+ubrazil+uperu
    total_MX=total_USD*17.06

    total_USD=round(total_USD,2)
    total_MX=round(total_MX,2)
    print(f"USD: {total_USD}")
    print(f"MXN: {total_MX}")


if __name__=="__main__":
    main()
