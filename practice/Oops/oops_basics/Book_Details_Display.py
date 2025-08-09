class Book:

  def __init__(self,title,author,price):
    self.title=title
    self.author=author
    self.price=price

  def display(self):
    print("Book Details:".center(50,'*'))
    print(f"Book Title: {self.title}\nBook Author: {self.author}\nBook Price: ${self.price}\n")


b1=Book('xyz','abc',45678)
b2=Book('pqr','tyu',657)
b3=Book('erty','fghj',567)
b4=Book('fghj','vhbjn',2133)

b1.display()
b2.display()
b3.display()
b4.display()
