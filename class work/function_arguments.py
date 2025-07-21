#positioning arguments
def display(name,email,pwd):
    print(name,email,pwd)
name,email,pwd='goutham','goutham@gmail.com','goutham@2507'
display(name,email,pwd)

#keyword arguments
def display(name,email,pwd):
    print(name,email,pwd)
display(name="goutham",email="gou@gmail.com",pwd="gou@123")

#default arguments
def display(name,email,pwd,age=21):
    print(name,email,pwd,age)
display(name="gou",email="gou@gmail.com",pwd="gou@123")
    

#variable arguments(keyword)
def display(**var):
    print(var)
display(name="gou",email="gou@gmail.com",pwd="gou@123")


#variable arguments(non keyword)
def display(*var):
    print(var)
display("gou","gou@gmail.com","gou@123")