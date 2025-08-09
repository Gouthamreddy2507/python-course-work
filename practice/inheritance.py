#single
class Parent:
    def func1(self):
        print("this is parent class")
class Child(Parent):
    def func2(self):
        print("this is child class")
obj = Child()
obj.func2()
obj.func1()

print("-------------------------")

#multilevel
class Parent:
    def func1(self):
        print("this is parent class")
class Child(Parent):
    def func2(self):
        print("this is child class")
class GrandChild(Child):
    def func3(self):
        print("this is Grandchild class")
obj = GrandChild()
obj.func1()
obj.func2()
obj.func3()

print("-----------------------")

#multiple
class Parent:
    def func1(self):
        print("this is parent class")
class Child1(Parent):
    def func2(self):
        print("this is child1 class")
class Child2(Parent):
    def func3(self):
        print("this is child2 class")
obj =Child2()
obj.func1()
#obj.func2()
obj.func3()


print("---------------")


#hierechical
class Father:
    def func1(self):
        print("this is father class")
class Mother(Parent):
    def func2(self):
        print("this is mother class")
class Child(Father,Mother):
    def func3(self):
        print("this is child class")
obj =Child()
obj.func1()
obj.func2()
obj.func3()


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