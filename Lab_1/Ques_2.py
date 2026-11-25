choice = input()
number = input()

if choice == "D2B":
    number = int(number)
    binary = ""

    if number == 0:
        binary = "0"

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    print(binary)

elif choice == "B2D":
    decimal = 0
    power = 0
    valid = True

    for i in range(len(number) - 1, -1, -1):

        if number[i] == "0":
            decimal = decimal + 0 * (2 ** power)

        elif number[i] == "1":
            decimal = decimal + 1 * (2 ** power)

        else:
            valid = False
            break

        power = power + 1

    if valid:
        print(decimal)
    else:
        print("Invalid binary number")