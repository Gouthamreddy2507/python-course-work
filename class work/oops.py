class shopping:
    discount = 10
   

    @classmethod
    def update(cls,new_discount):
        cls.discount = new_discount
        print(f'{new_discount} is updated')

    def product(self,price,name):
        self.price = price
        self.name = name

    @staticmethod
    def check(price):
        print('$%.2f'%price)
        

user1 = shopping()
user2 = shopping()

print(shopping.check(2300))

print(user1.check(2300))

shopping.update(15)

user1.product(34000,"laptop")
user2.product(56000,"phone")

print(shopping.discount)
shopping.discount = 15
print(shopping.discount)

print(user1.price)
print(user2.price)