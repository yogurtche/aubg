# Create a dictionary called student and calculate the average of their grades


my_student ={"name": "Jorgo", "school": "AUBG", "grades": [100, 54, 69, 50]}


my_student["name"]
my_student["school"]


def my_func(my_student):
    average = sum(my_student["grades"])/len(my_student["grades"])
    return average


print(my_func(my_student))