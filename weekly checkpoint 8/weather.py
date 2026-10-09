def max_temperature(temperature):
    highest_temp = temperature[0]
    for _ in temperature:
        if _ > highest_temp:
            highest_temp = _

    print(f"high: {highest_temp}°")

def min_temperature(temperature):
    lowest_temp = temperature[0]
    for _ in temperature:
        if _ < lowest_temp:
            lowest_temp = _

    print(f"low: {lowest_temp}°")

def main():
    day1 = [26, 26, 26, 25, 24, 23 ,21, 21, 20]
    day2 = [19,19,18,18,17,17,16,16,18,20,22,24,25,26,27,27,27,27,26,25,23,22,21,20]
    day3 = [19,18,18,17,16,16,16,16,17,20,22,23,25,26,26,27]

    print('today')
    max_temperature(day1)
    min_temperature(day1)

    print("\ntomorow")
    max_temperature(day2)
    min_temperature(day2)

    print("\nday after tomorrow")
    max_temperature(day3)
    min_temperature(day3)


if __name__=="__main__":
    main()
