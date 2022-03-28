# def add_num(x,y):
#     return x+y


# num1 = int(input('>'))
# num2 = int(input('>'))

# print(add_num(num1,num2))


# def slugify(word):
#     return word.replace(" ", "-").lower()

# print(slugify('How do you cook'))


# def first_last(first, last):
#     a = first[:2]
#     b = last[-2:]
    
#     return a+b

# print(first_last('Adaobi', 'United'))


# a = lambda x : x +15
# print(a(30))

# a = 20
# b = 30

# tim = lambda a,b : a*b
# print(tim(a,b))

# numeric = lambda string : string.isnumeric()
# change_case = lambda string : string.swapcase()
# print(change_case("AdAobI"))



# step 1: get input from user
# name = input("File name\n>")

# #step 2: split and get the last element
# print(name.split(".")[-1])

# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n * factorial(n-1)


# print(factorial(5))

my_list = [23,43,12,57,96,24]

# trippled = list(map(lambda x : 3*x, my_list))
# squared = list(map(lambda x : x**2, my_list))
# print(trippled)
# print(squared)

# my_list.extend([2,4,3,24,4])
# # my_list.sort()
# my_list.insert(-1,"Inserted")
# print(my_list)

a = [2,3,4,2,[2,3,4,5, [4,52,2],5],24]

p = a[-1]
x = a[4][4][1]
print(p+x)


def largest(arr:list, k:int):
    """ This function returns the highest k values in an array: arr. """
    
    
    arr.sort(reverse=True)
    # print(arr)
    return arr[:k]

def smallest(arr:list, k:int):
    """ This function returns the lowest k values in an array: arr. """
    
    
    arr.sort()
    return arr[:k]


print(largest([1, 1, 1, 0, 0, 0, 2, -2, -2], 2))
