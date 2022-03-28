# a = ['A', 'quick', 'brown', 'fox', 'just', 'died.']

# b = " ".join(a)


# print(b.replace("brown", "white"))



# arr = [1,2,3,4,5,6]
# mean = sum(arr)/len(arr)
# mapped =map(lambda y : y**2, arr)

# print(list(mapped))


# age = int(input("Age:\n>"))

# print(f"You were born in {2022-age}")

# from math import sqrt
# import statistics

# print("Enter scores seperated by commas")
# scores = input(">").split(",")
# int_scores = list(map(int, scores))
# mean = sum(int_scores) / len(int_scores)
# range_ = max(int_scores) - min(int_scores)

# x_mean = map(lambda x : (x-mean)**2, int_scores)
# std = sqrt(sum(x_mean)/len(int_scores))
# variance = std**2

# # mean = statistics.mean(int_scores)
# # median_ = statistics.median(int_scores)
# # statistics.stdev(int_scores)

# print(f"Mean: {mean}")
# print(f"Range: {range_}")
# print(f"Standard Deviation: {std}")
# print(f"Variance: {variance}")



def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)


print(factorial(5))

def miles_to_kilo(miles):
    return miles*1.6

print(miles_to_kilo(50))

def dollar_to_naira(dollar):
    return dollar*593

print(dollar_to_naira(2000))