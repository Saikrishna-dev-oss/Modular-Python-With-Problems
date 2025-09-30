class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no
    

    def credit(self,amount):
        self.balance += amount
        print("Rs:",amount,"Credited Successfully")
        print("Total Balance :",self.get_balance())
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs:",amount,"debited Successfully")
        print("Total Balance :",self.get_balance())
    
    def get_balance(self):
        return self.balance
    

acc1 = Account(1186,12345)
acc1.credit(25)
acc1.debit(320)