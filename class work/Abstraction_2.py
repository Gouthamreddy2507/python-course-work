from abc import ABC , abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

class Foodorder(order):
    def process_order(self):
        print("Processing Food order: check chef availability, estimate time,")

    

