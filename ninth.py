
# eng = input(">")
# frn = input(">")

# if not any(ele.isalpha() for ele in eng) and not any(ele.isalpha() for ele in frn):
#     eng_set = set(eng.split())
#     frn_set = set(frn.split())
#     print(len(eng_set.union(frn_set)))
    
# else:
#     print("Invalid input")


# def check_femat(a,b,c,n):
    
#     if n>2 and a^n + b^n == c^n:
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn't work")
        

# def take_input():
#     print("Enter values for a, b, c, d")
#     a = int(input('>'))
#     b = int(input('>')) 
#     c = int(input('>'))
#     d = int(input('>')) 
#     check_femat(a,b,c,d)
    
# take_input()



### Dictionaries


# data = {
#     "name": 'Desmond',
#     "course":"Backend/Datascience",
#     "state":"Lagos"
# }

# data = {}

# print(data["name"])

# print("Enter your name:")
# name = input('>')
# print("Gender")
# gender = input('>')

# student_num = '4384348'
# data[student_num]= {
#     'gender' : gender,
#     'name':name
# }



# print(data.get("John"))
# data.values()
# data.items()

# data.update([("d", "k")])
# print(data)
# # ad = data.pop('d')

# # print(ad)

# del data['d']
# print(data)
# dict()

# print("Before")
# new_data = {
#     "name" : "Desmond Nnebue",
#     "class": "Data science",
#     "salary": "₤148059844"
# }
# print(new_data)
# Write a program to change the name to first name and last name. The output of new_data should be:

# new_data = {
#     "first_name" : "Desmond",
#     "last_name":"Nnebue",
#     "class": "Data science",
#     "salary": "₤148059844"
# }

##CORRECTION

# name = new_data.pop('name')
# first_name, last_name = name.split()
# new_data.update([("first_name", first_name),
#                  ('last_name', last_name)])
# print("\nAfter:")
# print(new_data)



# Write a program that creates a frequency dictionary. E.g: 
#     frequency = {
#         2: 3,
#         3: 6,
#         1: 8,
#     }
    
# After creating the frequency, sort the dictionary by order of frquencies.
# arranged = {
#     1:8,
#     3:6,
#     2:3
# }
from cv2 import sort


sample = [2,3,5,3,2,5,7,5,3,5,6,4,3,6,5,3,5,2,1,5,8,3,4,6,8,4,4,5,1,7,7,1]
freq = {}
for num in sample:
    freq[num] = freq.get(num, 0) + 1
    
# print(freq)


sample_set = set(sample)
# print(sample_set)
# print({i: sample.count(i) for i in sample_set})

a = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(dict(a))

