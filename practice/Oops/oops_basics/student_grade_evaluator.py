class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def result(self):
        self.avg = sum(self.marks)/len(self.marks)
        if self.avg<35:
            print(f"{self.name}'s report:\nAverage: {self.avg}\nExam status:Fail")
        else:
            print(f"{self.name}'s report:\nAverage: {self.avg}\nExam status:Pass")

goutham = Student("goutham",[90,80,85])
soul = Student("soul",[35,12,20])

goutham.result()
soul.result()
        