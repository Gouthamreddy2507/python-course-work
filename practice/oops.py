class Mobile:
    def __init__(self,Brand,battery,ram,camera,price):
        self.Brand = Brand
        self.battery = battery
        self.ram = ram
        self.camera = camera
        self.price = price
    
    def display(self):
        print("Brand:",self.Brand)
        print("battery:",self.battery)
        print("ram:",self.ram)
        print("camera:",self.camera)
        print("price:",self.price)
        print("--------------")

obj = Mobile("apple","4000","8gb","48mp","90000")
obj.display( )
obj = Mobile("oneplus","5000","8gb","48mp","90000")
obj.display( )

#super
class A:
    def __init__(self):
        print("class a")
    def func1(self):
        print("Father class")
class B(A):
    def __init__(self):
        print("class b")
        super().__init__()
    def func2(self):
        print("mother class")
obj =B()
