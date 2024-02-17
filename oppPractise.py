class bank:
    def __init__(self,balance=0,password=1123,aaa=222):
        self.balance=balance;
        self.password=password
        self.__aaa=aaa
        
    
    def userView(self,num):
        
        print("""
              1- if u want to deposit reply with 1
              2- if u want to withdraw reply with 2
              3- if u want to send reply with 3
              4- if u want to check balance reply with 4
              
              """)
        num=int(input("what u want to pereform "))
        if(num==1):
            print("deposit")
            self.deposit(2000)
            
        elif(num==2):
            print("withdrawal")
            
        elif(num==3):
            print("send")
            
            
    def deposit(self,amount):
        self.balance=amount+self.balance
        print(f"your new balance is {self.balance}")
        
    def withdrawal(self,withdraw):
        if(self.balance>withdraw):
            self.balance=self.balance-withdraw
            print(f"withdrawal successful {self.balance}")
        else:
            print("insufficient balance")
            
a1=bank()
a1.userView(2)



#ENCAPSULATION
class Atm:
    def __init__(self):
        self.__pin=""
        
        
    def get_pin(self):
        return self.__pin
        
abc=Atm()
abc.get_pin("222")
        
        
    
