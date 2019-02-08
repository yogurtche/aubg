# Create a method that checks if a number is odd or even and prints the result


def check_number(number1)


if number1 % 2 == 0:
    print("{} => I am an even number".format(number1))
    else:
        print("{} => I am an odd number".format(number1))

check_number(2)
check_number(19)

# Creat a task that prints user input if present in the follwing list:
# ["John", "Jack", "Jim", "Johnny"]


my_list = ["John", "Jack", "Jim", "Johnny"]


def my_func(username):
    if username in my_list:
        print(username)


my_func("John")
my_func("Deyan")
