class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} vehicle started.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
car1 = Car("Toyota", "Camry")
car1.start()
car1.show_info()