

# for i in range(50,1000, 10):
#     print(i+3)
    
    
# my_list = [3,2,3,4,5,3,2,4,5,1]

# for i in my_list:
#     print(i)
    
# print()

# for i in range(len(my_list)):
#     if my_list[i] == 3:
#         print(my_list[i], end="")
        
import random

my_list = []

# for ele in range(10000000000):
#     a = random.choice(range(50,100))
#     my_list.append(a)

# print(my_list)

# def is_even(n):
#     return n%2==0

# my_list = [random.choice(range(50,100)) for _ in range(100000)]
# print(len(my_list))


#TUPles

# print((0, 1,2,2000000,1) < (0, 3, 4))


def ages():
    return 4,3
# a,b,c=(0, 3, 4)

# age1, age2 = ages()

# print(age1)
# print(age2)


# def printall(*data):
#     print(type(data))

# li = [1,2,4,3,5,2,4,2,4,3,31,3,53,5,132,5,435,24,5,24,5,2,32,4,3,5]
# printall(li)


# li1 = [0,3,2,4]
# li2 = [1,7,9,6]

# print(list(zip(li1, li2)))



#SETs
# my_set = list(set([1,2,4,6,3,3,1,2,4,2,4]))
# print(my_set)

a = {1,2,4,5}
b = {3,2,7,8}

# c = 
# b.update(a)
# print(a.union(b))
# print(b)


# print(a.intersection(b))
# b.intersection_update(a)
# print(b)

# print(b.difference(a))

# b.difference_update(a)
# print(b)

# print(a.symmetric_difference(b))

# print(a)

print("Enter the french students roll number seperated by space")
french = set(input(">").split())
# print(french)
print("Enter the english students roll number seperated by space")
english = set(input(">").split())
# print(english)


fren_eng = english.symmetric_difference(french)

print("The total number of either english or french but not both is:", len(fren_eng))