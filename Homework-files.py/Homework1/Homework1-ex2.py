print("This is the notebook")


inputstring = input("You can start iputing entries:  ").split(",")
entrylist = list(inputstring)

print("You have the chance to:")
print("1. Input entries")
print("2. Delete entries")

action = input("Please choose what you want to do next: ")


if action == "1":
    inputaddstring = input().split(", ")
    entrylist.extend(inputaddstring)
    print(entrylist)


elif action == "2":
    inputremovestring = input().split(",")
    entrylist.remove(inputremovestring)


print(entrylist)
