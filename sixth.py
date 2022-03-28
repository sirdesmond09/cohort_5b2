# data = input(">>").split(',')
# int_data = map(int, data)
# odd_int = filter(lambda x: x%2==1,int_data)
# print(list(odd_int))


# def middle(arr):
#     return arr[1:-1]



# def median(arr):
#     arr.sort()
#     mid_point  = len(arr)//2
#     if len(arr)%2==0:
#         return (arr[mid_point] + arr[mid_point-1])/2
    
#     return arr[mid_point]


# a = [1,3,5,2]

# print(median(a))

# print("What is your exam score?")
# score = int(input(">"))

# if score <= 39:
#     print("F")
# elif score <= 49:
#     print("E")
# elif score <= 59:
#     print("D")
# elif score <= 69:
#     print("C")
# elif score <= 79:
#     print("B")
# elif score <= 100:
#     if score <= 90:
#         print("A-")
#     else:
#         print('A+')


# import random
# a = [3,2,5,6,8,7]

# print(f"Select any number from {a}.\nWe hope it doesn't end in tears.")
# com_choice = random.choice(a)
# random.shuffle(a)
# print("Guess the number:")
# user_choice = int(input(">"))

# if user_choice in a:
#     if user_choice == com_choice:
#         print("All power belong to you, comerade.")
#     else:
#         print("Arhhh, comerade. Be like you go try again o.")
# else:
#     print("Comerade no be so!")


text = """The programs we have written so far accept no input from the user. They just do the same thing every time.
Python provides a built-in function called input that stops the program and waits for the user to type something. When the user presses Return or Enter, the program resumes and input returns what the user typed as a string. In Python 2, the same function is called raw_input."""

sub_text = input("Enter text to search for:\n>").lower()

lowercase_text = text.lower()
found = lowercase_text.find(sub_text)
count = lowercase_text.count(sub_text)

if found != -1:
    print(f"{count} result(s) found!")
    new_text = text.replace(sub_text, sub_text.upper())
    print(new_text)
    
else:
    print(f"{count} result(s) found!")

# Fermat’s Last Theorem says that there are no positive integers a, b, and c such that a^n + b^n = c^n for any values of n greater than 2.
# 1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
# checks to see if Fermat’s theorem holds. If n is greater than 2 and   a^n + b^n = c^n the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”

# 2. Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem. 