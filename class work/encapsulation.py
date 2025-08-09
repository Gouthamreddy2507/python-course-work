
class details:
    def __init__(self,name,mail,pwd):
        self.name = name
        self._mail = mail
        self.__pwd = pwd

    def getpassword(self):
        return self.__pwd
        
    def setpassword(self,new_password):
        self.__pwd = new_password

sumanth = details("sumanth","sumanth@gmail.com","sumanth@123")

print(sumanth.name)
sumanth.name = "sanjay"
print(sumanth.name)

print(sumanth._mail)
sumanth._mail = "sanjay@gmail.com"
print(sumanth._mail)

print(sumanth.getpassword())
sumanth.setpassword("sanjay@123")
print(sumanth.getpassword())



print("------------------------------")


class bank:
    def __init__(self):
        self.name = "xyz"
        self._balance = 0

    @property
    def noresbalance(self):
        return self._balance
    
    @noresbalance.setter
    def balance(self,amount):
        self._balance += amount

b=bank()

print(b.balance)
b.balance = 3000
print(b.balance)

print(b.name)
b.name="abc"
print(b.name)



print("---------------------------------")
class instagram:
    def __init__(self,username,bio,account_status=False):
        self.username = username
        self._bio = bio
        self.__account_status = account_status

    def get_acc_status(self):
        return self.__account_status
    
    def set_acc_status(self,status):
        self.__account_status=status
    
    @property
    def bio(self):
        return self._bio
    
    @bio.setter
    def bio(self,new_bio):
        self._bio=new_bio

    

mohith = instagram("mohith","eat",False)

print(mohith.username)
mohith.username = "goutham"
print(mohith.username)

print(mohith.get_acc_status())
mohith.set_acc_status(True)
print(mohith.get_acc_status())

print(mohith.bio)
mohith.bio = "Coder"
print(mohith.bio)
        