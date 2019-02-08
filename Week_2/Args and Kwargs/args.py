# Create a function that can take unlimited number of names and print them


def test_var_args(f_arg, *argv):
    print("various names: " + f_arg)
    for arg in argv:
        print("another arg thorugh argv: " + arg)


        test_var_args('jorgo', 'mister', 'sister', 'love', 'exercise')



# Create a function that can take unlimited number of key-value pairs 
# and print it in the format: The value for X is Y