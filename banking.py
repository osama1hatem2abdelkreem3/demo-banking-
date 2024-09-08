import datetime as dt

class Bank_account():
    def __init__(self, account_number, account_name, balance):
        self.account_number = account_number
        self.account_name = account_name
        self.account_balance=balance
    def ADD_new_account(self):
        #create new file for each clint
        f=open(f"{self.account_name}.txt","a+")
        if "Account Name |Account Number |Date of operation | Balance " in f"{self.account_name}.txt":
          f.write(f"\n{self.account_name}\t|{self.account_number}\t|{dt.datetime.now()}|{self.account_balance}\n") 
        else:
         f.write(f"Account Name |Account Number |Date of operation | Balance ")
         f.write(f"\n{self.account_name}\t|{self.account_number}\t|{dt.datetime.now()}|{self.account_balance}\n")
        f.close()        
        print(f"new account added MR {self.account_name.title()} \nyour balance = {self.account_balance}")
    def deposit(self,deposit=0):
        self.deposit=deposit
        self.account_balance+=self.deposit
        f=open(f"{self.account_name}.txt","a+")
        f.write(f"\n{self.account_name}\t|{self.account_number}\t|{dt.datetime.now()}|{self.account_balance}\n")
        f.close()   
        print(f"applying for the deposit ={self.deposit} ")
        print(f"successful operation your balance now is {self.account_balance} ")
    def get_current_balance(self):
        print(f'current balance = {self.account_balance}')
    def withdrawal(self):
        pass      
        
new=Bank_account(112233,'osama',2000)
new.ADD_new_account()
new.deposit(2000)
