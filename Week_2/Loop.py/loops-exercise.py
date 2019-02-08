# Create methods that print all of the odd and even numbers in a list


def my_function():
    my_list = [1, 7, 15, 19, 8, 17, -3, 2, 22, 1024]

    
    for num in my_list:
        if num % 2 == 0:
            print("{} is even".format(num))
        else:
            print("{} is odd".format(num))


my_function()


# Second Task

def my_sec_func():
    my_name = input("What is your name?")


    cont = True


    while(cont):
        for letter in my_name:
            print(letter)


    decision = input("Do you want to continue doing this (y/n)?")


    if decision == "n":
        cont = False


my_sec_func()