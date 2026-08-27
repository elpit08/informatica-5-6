def main():
    layer = input("Descent atmospheric layer: ")


    if layer.lower() == 'exosphere':
        print("Your altitude level will be between 700-10,000 km")
        distance = int(input("Enter exact altitude: "))
        distance *= 1000
        desent_time = distance / 2000
        print(f"Total desent time: {desent_time}")

    elif layer.lower() == 'thermosphere':
        print("Your altitude level will be between 85-700 km")
        distance = int(input("Enter exact altitude: "))
        distance *= 1000
        desent_time = distance / 500
        print(f"Total desent time: {desent_time}")

    elif layer.lower() == 'mesosphere':
        print("Your altitude level will be between 50-85 km")
        distance = int(input("Enter exact altitude: "))
        distance *= 1000
        desent_time = distance / 200
        print(f"Total desent time: {desent_time}")

    elif layer.lower() == 'statosphere':
        print("Your altitude level will be between 12-50 km")
        distance = int(input("Enter exact altitude: "))
        distance *= 1000
        desent_time = distance / 75
        print(f"Total desent time: {desent_time}")

    elif layer.lower() == 'troposphere':
        print("Your altitude level will be between 0-12 km")
        distance = int(input("Enter exact altitude: "))
        distance *= 1000
        desent_time = distance / 20
        print(f"Total desent time: {desent_time}")


    else:

        print("Invalid response")




if __name__=="__main__":
    main()
