# import random

# bank_data = {}

# #creating other accounts
# name2 ="Bergs Gee"
# age2 = 20
# account_type2 = "Savings"
# balance2 = 0
# account_num2 = "0123456789"
# pin2 = "1234"

# user2_info = {}
# user2_info["name"] = name2
# user2_info['age'] = age2
# user2_info["acc_type"] = account_type2
# user2_info["pin"] = pin2
# user2_info["bal"] = balance2 

# bank_data[account_num2] = user2_info

# # print(bank_data)

# while True:
#     title = "WELCOME TO BANK OF NIGERIA"
#     print(title)
#     user = int(input("1. Register\n2. Login\n3. Exit\n::>> "))

#     if user == 1:
#       print("******REGISTER******")
#       name = input("Name\n:>> ")
#       age = int(input("Age\n:>> "))
#       acc = input("Account Type\n:>> ")
#       pin = input("Pin\n:>> ")

#       user_info = {}
#       number =  [0,1,2,3,4,5,6,7,8,9]
#       account_num = "0"
#       account_num += "".join([str(random.choice(number)) for _ in range(9)])
      
#       balance = 0
#       user_info["name"] = name
#       user_info["age"] = age
#       user_info["acc_type"] = acc
#       user_info["bal"] = balance
#       user_info["pin"] = pin
      
#       bank_data[account_num] = user_info
      
#       print(f"\nHello {name.title()}, your account has been created successfully. Your account number is {account_num}. Please do not disclose your pin to anyone.\nThank you for choosing BON")
#     #   print(bank_data)
#     elif user == 2:
#         print("*******LOGIN******")
#         acc_nu = input("Account Number\n:>> ")
#         p_num = input("PIN\n:>> ")
        
#         user_data = bank_data.get(acc_nu)
#         # print(user_data)
#         if user_data and user_data['pin']==p_num:
#             while True:    
#               print("****WELCOME****")
#               user_select = input("\n1. Deposit\n2. Withdrawal \n3. Transfer\n4. Check Balance\n5. Exit\n:>> ")
#               if user_select == "1":
#                 print("******DEPOSIT******")
#                 deposit_amount = int(input("Enter amount you want to deposit\n:>> "))  
#                 if deposit_amount <= 0:
#                     print("Amount must be greater than 0")
#                 else:
#                  user_data['bal'] += deposit_amount
                 
#                  print("\nDeposit Successful!!!\nYour new account balance is $%i\n"%user_data["bal"])

#               elif user_select == "2":
#                   print("******WITHDRAWAL******")
#                   amount = int(input("Enter Amount you want to withdraw\n:>> "))
                  
#                   if amount >= user_data['bal']:
#                       print("Insufficient Funds")
#                   else:   
#                    user_data['bal'] -= amount
#                    print("\nWithdrawal Successful!!!\nYour account balance is $%i"%user_data['bal'])
              
#               elif user_select == "3":
#                   print("******TRANSFER******") 
#                   other_acc = input("Enter Account number\n:>> ")
#                   trans_amount = int(input("Enter Amount you want to Transfer\n:>> "))
                  
#                   beneficiary = bank_data.get(other_acc)
#                 #   print(beneficiary)
#                   if beneficiary:
#                     if trans_amount >= user_data['bal']:
#                       print("Insufficient Funds")
#                     else:   
#                       user_data['bal'] -= trans_amount
#                       beneficiary['bal'] += trans_amount
                      
#                       print("\nTransfer Successful!!!\nYour account balance is $%i"%user_data['bal'])
                      
#                   else:
#                    print("Unable to process transfer.\nAccount number is not valid") 
              
#               elif user_select == "4":
#                   print("******BALANCE******")
#                   print("Your Balance is $%i"%user_data['bal'])        
                
#               elif user_select == "5":
#                 break   
#               else:
#                   print("Invalid Selection") 
#         else:
#             print("Invalid Details")        
    
      
#     elif user == 3:
#         break
#     else:
#         print("Invalid Selection")
        
# print("**THANK YOU FOR BANKING WITH US**")   


# file = open("file.txt", 'a')
# file.write("\nThis is something else.")
# file.close()


# file = open("file.txt")
# data = file.read()
# file.close()


# print(data)


import random
data_file = open("guess_database.txt", "r")
data = eval(data_file.read())
data_file.close()



score = 0
trial = 3
while True:
    name = input("What is your name\n::>> ").lower()
    data[name] = data.get(name, 0)
    
    while trial >0:
        trial -=1
        a = [3,2,5,6,8,7]
        print(f"Select any number from {a}.\nWe hope it doesn't end in tears.\n")
        com_choice = random.choice(a)
        random.shuffle(a)
        print("Guess the number:")
        user_choice = int(input(">"))

        if user_choice in a:
            if user_choice == com_choice:
                
                trial +=1
                score+=2
                print("Correct!")
                print(f"{trial} trial(s) remaining!")
                
            else:
                print("Incorrect")
                print(f"{trial} trial(s) remaining!")
        else:
            print("Comrade no be so!")
            print(f"{trial} trial(s) remaining!")
            

        if trial==0:    
            print("Game over")
            print(f"Your score is {score}\n") 
            if score > data[name]:
                data[name] = score
                print(f"You have a new high score of {score}")
     
    print("\nDo you want to try again?(Y/n)")
    choice = input(">").lower()
    if choice == 'y':
        trial = 3
        continue
    else:
        print("Game over!")
        break


file = open("guess_database.txt", "w")
file.write(str(data))
file.close()
    
    

