# val = "This is a string"
# val2 = " and another string."
# print(val + val2)

# name = "Adebowale"
# print(name[3])


# variable = input(">")

# print(f"My name is {variable}")

# a = 14
# b = 35

# print(f"The sum of {a} and {b} is {a+b}. This is a simple mathematical operation with python.\n\tRegards\n\tDesmond")

# print("I am my mother's son")
# print('Joseph said, "I cannot do this anymore". ')

# my_string = "this is A stRing"

# print(my_string.rindex("i",0,10))

# num = 1
# print(bool(num))
# val = True
# print(int(val))


# length = int(input("Enter the length of the square\n>"))
# print(f"The area of a square with length of {length}cm is {length**2}cm²")


# p = int(input("Initial capital:\n>"))
# r = int(input("Rate (in percentage e.g 80 for 80%):\n>"))
# t = int(input("Time in years:\n>"))

# r/=100

# interest = p*r*t
# print(f"Investing ${p} at a rate of {r*100}% would give an interest of {interest} after {t} years")


first_name = input("First Name:\n>")
last_name = input("Last Name:\n>")
username = (first_name[0:3] + last_name[0:3]).lower()

print(f"Hello {first_name}, your username is {username}.")
