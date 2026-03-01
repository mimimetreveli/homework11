#1
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount<=0:
            print("amount has to be positive")
            return
        if self.balance+amount>2500:
            print("you can not deposit over 2500:")
        else:
            self.balance+=amount

    def withdraw(self, amount):
        if amount<=0:
            print("amount has to be positive")
            return
        if amount>self.balance:
            print("not enough money")
        else:
            self.balance-=amount

    def display_balance(self):
        print(f"{self.owner} balance: {self.balance}")

account=BankAccount("Mimi", 2000)
account.deposit(400)
account.withdraw(100)
account.display_balance()

#2
import math
class Shape:
    def describe(self):
        print("I am a shape")

class Polygon(Shape):
    def __init__(self, *sides):
        self.sides=sides

class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.a=a
        self.b=b
        self.c=c

    def calculate_area(self):
        p=(self.a+self.b+self.c)/2
        area=math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return area

triangle=Triangle(12, 40, 16)
triangle.describe()
print(f"triangle area: {triangle.calculate_area()}")