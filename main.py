  
import json
import random
import string
from pathlib import Path


class Bank:
    database="data.json"
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.load(fs)
        else:
            print("no such file exist")   
    except Exception as e:
        print(f"error{e}")

    @classmethod
    def update(cls):
        with open(Bank.database, "w") as fs:
            json.dumps(Bank.data, fs, indent=4) 

    @classmethod
    def accountno(cls):
        ls=[]

        number=random.choices(string.digits,k=3)
        special= random.choices(string.punctuation,k=2)
        alphaL=random.choice(string.ascii_lowercase)
        alphaU=random.choices(string.ascii_uppercase,k=3)

        ls.extend(number)
        ls.extend(special)
        ls.append(alphaL)
        ls.extend(alphaU)
        random.shuffle(ls)

        return "".join(ls)
        


    def create_account(self):
        info={
            "name": input("Your name? "),
            "age": int(input("your age? ")),
            "email": input("your email? "),
            "mobile": int(input("enter your phone number: ")),
            "pin": int(input("Generate a 4 number pin? ")),
            "account": Bank.accountno(),
            "balance": 0,
        }

        if info["age"] < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create account ")
        else:
            print("account created succesfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("note down your account number")

            Bank.data.append(info)
            Bank.update()


    def money_deposit(self):
        acc=input("enter your account number")
        pin=int(input("enter pin"))

        for i in Bank.data:
            if i["account"]== acc:
                found=True
                if i["pin"]== pin:
                    print(f"access granted")
                    amount =int(input("enter the amount of money u want to deposit: "))
                    i["balance"]+= amount

                    Bank.update()
                    print(f"balance added succesfully")
                    print("your total balance is",i["balance"])

                else:
                    print("wrong pin")
        if not found:
            print("no such account exist")
        

    def money_withdraw(self):
        acc=input("enter your account number")
        pin=int(input("enter pin"))

        for i in Bank.data:
            if i["account"]== acc:
                found=True
                if i["pin"]== pin:
                    print(f"access granted")
                    amount =int(input("enter the amount of money u want to withdrawn: "))
                    if i["balance"]>= amount:
                        i["balance"]-= amount
                    else:
                        print("insufficient bank balance")

                    Bank.update()
                    print(f"balance added succesfully")
                    print("your total balance is", i["balance"])

                else:
                    print("wrong pin")
        if not found:
            print("no such account exist")
        
    def details(self):
        acc=input("enter your account number")
        pin=int(input("enter pin"))

        for i in Bank.data:
            if i["account"]== acc:
                found=True
                if i["pin"]== pin:
                    print(f"access granted")
                    for j in i:
                        print(f"{j}: {i[j]}")

                else:
                    print("wrong pin")
        if not found:
            print("no such account exist")

    def update_details(self):
        acc=input("enter your account number")
        pin=int(input("enter pin"))

        for i in Bank.data:
            if i["account"]== acc:
                found=True
                if i["pin"]== pin:
                    print(f"access granted")
                    for j in i:
                        print(f"{j}: {i[j]}")

                    change= input("what do you want to change?")
                    new_value=input("changed information")

                    if change in ["name","email","mobile"]:
                        i[change]= new_value
                        Bank.update()
                    else:
                        print("either you cannot change these details or these details don't exist")
                else:
                    print("wrong pin")
        if not found:
            print("no such account exist")
        
    def delete_account(self):
        acc=input("enter account u want to remove")
        pin=int(input("enter pin"))

        for i in Bank.data:
            if i["account"]== acc:
                found=True
                if i["pin"]== pin:
                    confirmation= input("are u sure u want to delete this account(YES/NO)? ").lower()
                    if confirmation == "yes":
                        Bank.data.remove(i)
                        Bank.update()
                        print("data deleted succesfully")
                    else:
                        print("account is not deleted..")
                else:
                    print("wrong pin")
        if not found:
            print("no such account exist")




user= Bank()

print("Press 1 for creating a bank account")
print("press 2 for depositiong money in your bank account")
print("Press 3 for withdrawing money from your bank account")
print("Press 4 to see details")
print("Press 5 to update those details")
print("Press 6 for deleting your bank account")
print("To exit print exit")

while True:
    choose=input("what operation u want to perform?")
    if choose.isdigit():
        if choose == "1":
            user.create_account()
        elif choose =="2":
            user.money_deposit()
        elif choose=="3":
            user.money_withdraw()
        elif choose == "4":
            user.details()
        elif choose == "5":
            user.update_details()
        elif choose == "6":
            user.delete_account()
        else:
            print("Error wrong number entered")
            continue
    else:
        if choose == "exit":
            break
        else:
            print("please choose a number from options only")
