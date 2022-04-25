# from datetime import datetime

# today = datetime.now()
# print(today)
# # print(today.isoweekday())
# # print(type(today))
# sting_date = today.strftime("The time is %H:%Mam on %A %dst of %B %Y.")
# # print(sting_date)

# to_date = datetime.strptime("21-April-22", "%d-%B-%y" )

# print(to_date)

###### OOP #####

from datetime import datetime


class Human():
    creator = "God"
    
    def __init__(self, name:str, yob:int):
        
        self.name = name
        self.year = yob

    def walk(self):
        walk_ =  f""" {self.name}
         O
       / | \\
         |
        / \\
        \  \ 
        
        """
        return walk_  
    
    def __age(self):
        current_year = datetime.now().year
        return current_year-self.year
    
    def desc(self):
        return f"This is {self.name} and he/she is {self.__age()} years old. He/she was born in the year {self.year}."
    

# print(Human.creator)

human1 = Human("David", 1999 )
# human2 = Human("Mercy", 2001)

print(human1.walk())