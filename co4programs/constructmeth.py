class bank:
    def __init__(self,accNo,name,accType,balance=0):
     self.accNo=accNo
     self.name=name
     self.accType=accType
     self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposit successful!new balance:{self.balance}")
        else:
            print("invalid deposit amount.enter a positive value.")
    def withdraw(self,amount):
        if amount>0:
            if amount<=self.balance:
                self.balance-=amount
                print(f"new balance:{self.balance}")
            else:
                print("insufficient balance.")
        else:
            print("invalid withdrawal amount.enter a positive value.")
    def display(self):
        print("\nAccount Number:",self.accNo)
        print("Account Holder Name:",self.name)
        print("Account Type:",self.accType)
        print("Balance:",self.balance)
b1=bank(1002,"Nidhi","savings",0)
b1.display()
while True:
    print("\n***MENU***")
    print("1.deposit")
    print("2.withdraw")
    print("3.display")
    print("4.exit")
    choice=int(input("\nenter your choice(1-4):"))
    if choice==1:
        d=float(input("enter amount to be deposited:"))
        b1.deposit(d)
    elif choice==2:
        w=float(input("enter amount to withdraw:"))
        b1.withdraw(w)
    elif choice==3:
        b1.display()
    elif choice==4:
        print("exit")
        break
    else:
        print("enter a valid choice.")
    
