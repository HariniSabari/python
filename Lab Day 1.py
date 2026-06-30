#Que 1
#Arithmetic
a=int(input("enter a number:"))
b=int(input("enter b number:"))
print("Add:",a+b)
print("Sub:",a-b)
print("Mult:",a*b)
print("Div:",a/b)
print("Mod:",a%b)
print("FD:",a//b)
print("Expo:",a**b)

#Que 2
#Area and Perimeter
#Rectangle
Length=int(input("enter Length:"))
Breadth=int(input("enter Breadth:"))
Area=Length*Breadth
Perimeter=2*(Length+Breadth)
print("Area:",Area)
print("Perimeter:",Perimeter)
#Square
Side=int(input("enter Side:"))
Area=Side**2
Perimeter=4*Side
print("Area:",Area)
print("Perimeter:",Perimeter)
#Circle
Radius=int(input("enter Radius:"))
Area=Radius**2
Perimeter=3*Radius
print("Area:",Area)
print("Perimeter:",Perimeter)

#Que 3
#Average
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
Average=(a+b+c)/3
print("Average:",Average)

#Que 4
#Equal
a=int(input("enter a number:"))
b=int(input("enter b number:"))
print("Equal:",a==b)
print("a Greater than b:",a>b)
print("a less than or equal to b:",a<=b)

#Que 5
#Square Root
s=int(input("enter a number:"))
print("Square Root:",s**2)

#Que 6
#Simple and Compound Interest
p=int(input("enter a Principle Amount:"))
r=int(input("enter a Rate of Interest:"))
t=int(input("enter a Time:"))
SimpleInterest=(p*r*t)/100
CompoundInterest=p*((1+r/100)**t)-p
print("Simple Interest:",SimpleInterest)
print("Compound Interest:",CompoundInterest)

#Que 7
#Assignment
x=10
x+=5
print("After +5:",x)
x-=3
print("After -3:",x)
x*=2
print("After *2:",x)
x/=4
print("After /4:",x)
x%=2
print("After %2:",x)
x**=3
print("After **3:",x)

#Que 8
#Swapping
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))

a = a + b
b = a - b
a = a - b

print("After Swapping:")
print("a =", a)
print("b =", b)

#Que 9
#Username and Password
username = input("Enter username:")
password = input("Enter password:")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")

#Que 10 
#Cube Rate
num = int(input("Enter a number:"))
cube_root = num ** (1/3)
print("Cube Root =", cube_root)
