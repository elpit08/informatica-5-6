def main():
    layer = input("Descent atmospheric layer: ")


    if layer.lower() == 'exosphere':
        print("Your altitude level will be between 700-10,000 km")
        distance = float(input("Enter exact altitude: "))
        distance *= 1000
        exo = (distance - 700000) / 2000
        therm = (700000 - 85000) / 500
        mesos = (85000 - 50000) / 200
        strato = (50000 - 12000) / 75
        tropo = 12000 / 20
        desent_time = round(exo + therm + mesos + strato + tropo,1)

        print(f"Total desent time: {desent_time}")

    elif layer.lower() == 'thermosphere':
        print("Your altitude level will be between 85-700 km")
        distance = float(input("Enter exact altitude: "))
        distance *= 1000
        therm = (distance - 85000) / 500
        mesos = (85000 - 50000) / 200
        strato = (50000 - 12000) / 75
        tropo = 12000 / 20

        desent_time = round(therm + mesos + strato + tropo,1)
        print(f"Total desent time: {desent_time}")

    elif layer.lower() == 'mesosphere':
        print("Your altitude level will be between 50-85 km")
        distance = float(input("Enter exact altitude: "))
        distance *= 1000
        mesos = (distance - 50000) / 200
        strato = (50000 - 12000) / 75
        tropo = 12000 / 20

        desent_time = round(mesos + strato + tropo,1)
        print(f"Total desent time: {desent_time}")

    elif layer.lower() == 'statosphere':
        print("Your altitude level will be between 12-50 km")
        distance = float(input("Enter exact altitude: "))
        distance *= 1000
        strato = (distance - 12000) / 75
        tropo = 12000 / 20

        desent_time = round(strato + tropo,1)
        print(f"Total desent time: {desent_time}")

    elif layer.lower() == 'troposphere':
        print("Your altitude level will be between 0-12 km")
        distance = float(input("Enter exact altitude: "))
        distance *= 1000
        desent_time = round(distance / 20,1)
        print(f"Total desent time: {desent_time}")


    else:
        print("Invalid response")


if __name__=="__main__":
    main()
