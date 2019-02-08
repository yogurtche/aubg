def add(a, b):
    return a+b


def substract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def sumcount(list):
    sum = 0
    for a in list:
        sum += a
    return sum


print("Operation: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Sum and count numbers")


operation = input("Select one of the operations 1, 2, 3, 4, 5")


number1 = int(input("First number: "))
number2 = int(input("Second number: "))

if operation == "1":
    print(add(number1, number2))


elif operation == "2":
    print(substract(number1, number2))


elif operation == "3":
    print(multiply(number1, number2))


elif operation == "4":
    print(divide(number1, number2))


elif operation == "5":
    input_string = input("Enter an element for the list separated by ',' ")
    list = input_string.split(",")
    print("Calculating sum and count of the elements from the input list")
    sum = 0
    for num in list:
        sum += int(num)
    print("Sum = ", sum)
print("You entered these", len(list), "elements.")
