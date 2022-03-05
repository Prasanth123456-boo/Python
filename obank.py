class Customer:
    def getData(self,name,accno,acctype,balance):
        self.name=name
        self.accno=accno
        self.acctype=acctype
        self.balance=balance
    def displayCustomer(self):
        print("customer name:",self.name)
        print("account number:",self.accno)
        print("account type:",self.acctype)
        print("balance account:",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdrawal(self,amount):
        if self.balance-amount<0:
            print("insufficient funds")
        else: self.balance=self.balance-amount

ch=0
while ch!=5:
    print("1.new customer")
    print("2.deposit")
    print("3.withdrawal")
    print("4.display")
    print("5.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        obj=Customer()
        n=input("enter name")
        no=int(input("enter account number:"))
        t=input("enter account type(sb/c):")
        b=int(input("enter the amount"))
        obj.getData(n,no,t,b)
    if ch==2:
        b=int(input("enter the amount to be deposited: "))
        obj.deposit(b)
    if ch==3:
        b=int(input("enter the amount to be withdrawn: "))
        obj.withdrawal(b)
    if ch==4:
        obj.displayCustomer()
    else:print("program terminated")     

        
    
