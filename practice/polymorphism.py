#polymorphism is a concept of object oriented programming, which means multiple forms or more than one form
#1.compile time 
#2.method over loading- same class ,same func or method name ,diff para
#3.run time/dynamic
#2.method over riding - diff class, same name ,diff para

#method overloading
class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=1):
        return a+b+c
obj = A()
print(obj.sum(1,2,5))

print("------------------")
#method over riding
class A:
    def display(self):
        print("this is class A")
class B(A):
    def display(self):
        print("this is class B")
        super().display()
obj = B()
obj.display()
    