import random
from datetime import datetime

file = open("customers.txt", "r")
dataset = file.readlines()
customer, transaction = eval(dataset[0]), eval(dataset[1])
file.close()




while True:
    title = "WELCOME TO BANK OF NIGERIA"
    # print(title)
    user = int(input("1. Register\n2. Login\n3. Exit\n::>> "))

    if user == 1:
      print("******REGISTER******")
      name = input("Name\n:>> ")
      age = int(input("Age\n:>> "))
      acc = input("Account Type\n:>> ")
      pin = input("Pin\n:>> ")

      user_info = {}
      number =  [0,1,2,3,4,5,6,7,8,9]
      account_num = "0"
      account_num += "".join([str(random.choice(number)) for _ in range(9)])
      
      balance = 0
      user_info["name"] = name
      user_info["age"] = age
      user_info["acc_type"] = acc
      user_info["bal"] = balance
      user_info["pin"] = pin
      user_info['is_active'] = True
      
      customer[account_num] = user_info
      transaction[account_num] = []
      
      print(f"\nHello {name.title()}, your account has been created successfully. Your account number is {account_num}. Please do not disclose your pin to anyone.\nThank you for choosing BON")
    #   print(customer)
    elif user == 2:
        print("*******LOGIN******")
        acc_num = input("Account Number\n:>> ")
        p_num = input("PIN\n:>> ")
        
        user_data = customer.get(acc_num)
        # print(user_data)
        if user_data and user_data['pin']==p_num and user_data['is_active']==True:
            while True:    
              print("****WELCOME****")
              user_select = input("\n1. Deposit\n2. Withdrawal \n3. Transfer\n4. Check Balance\n5. See recent transactions\n6. Deactivate Account\n7.Logout\n:>> ")
              if user_select == "1":
                print("******DEPOSIT******")
                deposit_amount = int(input("Enter amount you want to deposit\n:>> "))  
                if deposit_amount <= 0:
                    print("Amount must be greater than 0")
                else:
                 user_data['bal'] += deposit_amount
                 trans_record ={"amount":deposit_amount,
                                "status":"credit",
                                "action":"deposit",
                                "trans_date":str(datetime.now())}
                 transaction[acc_num].append(trans_record)
                 print("\nDeposit Successful!!!\nYour new account balance is $%i\n"%user_data["bal"])

              elif user_select == "2":
                  print("******WITHDRAWAL******")
                  amount = int(input("Enter Amount you want to withdraw\n:>> "))
                  
                  if amount >= user_data['bal']:
                      print("Insufficient Funds")
                  else:   
                   user_data['bal'] -= amount
                   trans_record ={"amount":amount,
                                "status":"debit",
                                "action":"withdraw",
                                "trans_date":str(datetime.now())}
                   transaction[acc_num].append(trans_record)
                   
                   print("\nWithdrawal Successful!!!\nYour account balance is $%i"%user_data['bal'])
              
              elif user_select == "3":
                  print("******TRANSFER******") 
                  other_acc = input("Enter Account number\n:>> ")
                  trans_amount = int(input("Enter Amount you want to Transfer\n:>> "))
                  
                  beneficiary = customer.get(other_acc)
                #   print(beneficiary)
                  if beneficiary and beneficiary['is_active']==True:
                    if trans_amount >= user_data['bal']:
                      print("Insufficient Funds")
                    else:   
                      user_data['bal'] -= trans_amount
                      trans_record ={"amount":trans_amount,
                                "status":"debit",
                                "action":"transfer",
                                "trans_date":str(datetime.now())}
                      transaction[acc_num].append(trans_record)
                      
                      beneficiary['bal'] += trans_amount
                      trans_record ={"amount":trans_amount,
                                "status":"credit",
                                "action":"transfer",
                                "trans_date":str(datetime.now())}
                      transaction[other_acc].append(trans_record)
                      
                      print("\nTransfer Successful!!!\nYour account balance is $%i"%user_data['bal'])
                      
                  else:
                   print("Unable to process transfer.\nAccount number is not valid") 
              
              elif user_select == "4":
                  print("******BALANCE******")
                  print("Your Balance is $%i"%user_data['bal'])        
              elif user_select == "5":
                  trans = transaction.get(acc_num)[-5:] 
                  print(f"Current balance is: ${user_data['bal']}") 
                  for tran in trans:
                      print("="*8)
                      print("Amount:", "$"+str(tran["amount"]))
                      print("Status:", tran["status"].title())
                      print("Action:", tran["action"].title())
                      print("Date:", tran["trans_date"])
                      print("="*8)
              
              elif user_select == "6":
                print("You are about to deactivate your account. If you are sure about this then enter your pin to continue. Else press enter to skip.")
                pin = input(">")
                if user_data['pin'] == pin:
                    user_data['is_active'] = False
                    break
              elif user_select == "7":
                break   
              else:
                  print("Invalid Selection") 
        else:
            print("Invalid Details")        
            
    elif user == 3:
        break
    else:
        print("Invalid Selection")
        
print("**THANK YOU FOR BANKING WITH US**")  
 
file = open("customers.txt", "w")
customer = file.writelines([str(customer)+ "\n", str(transaction)])
file.close()