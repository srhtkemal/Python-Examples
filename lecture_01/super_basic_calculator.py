def addition(first_number, second_number):
    result = first_number+second_number
    return result


def subtraction(first_number, second_number):
    result = first_number-second_number
    return result


def multiplication(first_number, second_number):
    result = first_number*second_number
    return result


def division(first_number, second_number):
    if (second_number != 0):
        result = first_number/second_number
        return result
    else:
        return "You know you can't subtract to zero."


def mod(first_number, second_number):
    if (second_number != 0):
        result = first_number % second_number
        return result
    else:
        return "You know you can't subtract to zero."


print("Welcome to the super basic calculator. ")

while (True):
    first_number = input(
        "Press 'q' to quit. \nPlease write your first number: ")

    if (str(first_number).lower() == "q"):
        break
    second_number = input("Your second number: ")

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except:
        print("At least one of your numbers is wrong")

    operation_number = input("Enter the number of the arithmetic operation you want to perform: \n"
                             "1: addition\n"
                             "2: subtraction\n"
                             "3: multiplication\n"
                             "4: division\n"
                             "5: mod\n")
    try:
        operation_number = int(operation_number)
    except:
        print("Your operation number is not a number")

    if (operation_number > 0 and operation_number < 6):
        if (operation_number == 1):
            print(addition(first_number, second_number))
        elif (operation_number == 2):
            print(subtraction(first_number, second_number))
        elif (operation_number == 3):
            print(multiplication(first_number, second_number))
        elif (operation_number == 4):
            print(division(first_number, second_number))
        elif (operation_number == 5):
            print(mod(first_number, second_number))
        else:
            print("An error has acquired")
    else:
        print("Your operation number is not valid")
    print("Wanna try again? ")
print("See ya!")
