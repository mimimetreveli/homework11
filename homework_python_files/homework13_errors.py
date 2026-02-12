#1
while True:
    try:
        num1=int(input("num1: "))
        num2=int(input("num2: "))
        print(num1/num2)
        break
    except ValueError:
        print("enter a number")
    except ZeroDivisionError:
        print("cant divide by zero")
#2
def divide_numbers(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "cant divide by zero"
    except TypeError:
        return "invalid input"

print(divide_numbers(10,2))
print(divide_numbers(5,0))
print(divide_numbers("a",3))
#3
nums=[1,2,3]
try:
    index=int(input("enter index"))
    print(nums[index])
except IndexError:
    print("index out of range")
except ValueError:
    print("enter a number")
#4
try:
    with open("myresult.txt") as obj:
       print(obj.read())
except FileNotFoundError:
    print("file not found")
#5
import math
try:
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    c=int(input("enter c: "))
    if a==0:
        raise ValueError("not a quadratic equation")
    D=b**2-4*a*c
    if D<0:
        raise ValueError("discriminant is negative, no real root")
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print(x1,x2)
except ValueError as e:
    print(e)
#6
try:
    a=int(input("enter a:"))
    b=int(input("enter b: "))
    c=int(input("enter c: "))
    if a+b>c and a+c>b and b+c>a:
        avg=(a+b+c)/3
        print(avg)
    else:
        raise ValueError("cant create a triangle")
except ValueError as e:
    print(e)

