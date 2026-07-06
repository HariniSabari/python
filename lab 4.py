#break
#Task1
'''for i in range(1,101):
    if i ==51:
        break
    print(i)
#Task2
while True:
    password=input("enter password:")
    if password=="admin123":
        print("correct password")
        break
    else:
        print("wrong password")
#Task3
names=['keerthi','sakthi','harini','bawa']
search=input("enter name:")
for name in names:
    if name in name==search:
        print("name found")
        break

#continue
#Task4
for i in range (1,51):
    if i %3==0:
        continue
    print(i)
#Task5
for i in range(1,51):
    if i %2==0:
        continue
    print(i)
    
#Task6
text=input("enter a word:")
for ch in text:
    if ch in "aeiouAEIOU":
        continue
    print(ch)
#pass
#task7
def display():
    pass
#task8
class student:
    pass
#task9
for i in range(1,6):
    if i ==3:
        pass
    print(i)


#while loop
i=1
while i <=100:
    if i ==51:
        break
    print(i)
    i+=1
while True:
    pwd = input("Enter Password: ")
    if pwd == "1234":
        print("Correct Password")
        break
names = ["jothi", "harini", "sakthi", "Keerthika"]
search = input("Enter Name: ")
i = 0
while i < len(names):
    if names[i] == search:
        print("Name Found")
        break
    i += 1
i = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
i=1
while i <=50:
    if i %2==0:
        i+=1
        continue
    print(i)
    i+=1
word = input("Enter Word: ")
i = 0
while i < len(word):
    if word[i] in "aeiouAEIOU":
        i += 1
        continue
    print(word[i])
    i += 1
i=1
while i<=5:
    if i ==3:
        pass
    print(i)
    i+=1'''
#while loop
#1
'''i = 1
while i <= 10:
    print(i)
    i += 1
#2
i = 10
while i >= 1:
    print(i)
    i -= 1
#3
i = 2
while i <= 20:
    print(i)
    i += 2
#4
i = 1
while i <= 20:
    print(i)
    i += 2
#5
i = 1
s = 0

while i <= 50:
    s += i
    i += 1

print(s)
#6
n = int(input())
i = 1

while i <= 10:
    print(n * i)
    i += 1
#7
n = int(input())
count = 0

while n > 0:
    count += 1
    n //= 10

print(count)
#8
n = int(input())
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)
#9
n = int(input())
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
#10
n = int(input())
s = 0
p = 1

while n > 0:
    d = n % 10
    s += d
    p *= d
    n //= 10

if s == p:
    print("Spy")
else:
    print("Not Spy")
#11
n = int(input())
s = 0

while n > 0:
    s += n % 10
    n //= 10

print(s)
#12
n = int(input())
p = 1

while n > 0:
    p *= n % 10
    n //= 10

print(p)
#13
n = int(input())
temp = n
s = 0

while n > 0:
    d = n % 10
    s += d ** 3
    n //= 10

if temp == s:
    print("Armstrong")
else:
    print("Not Armstrong")'''

'''n = int(input())
large = 0

while n > 0:
    d = n % 10
    if d > large:
        large = d
    n //= 10

print(large)

n = int(input())
small = 9

while n > 0:
    d = n % 10
    if d < small:
        small = d
    n //= 10

print(small)

n = int(input())

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1

n = int(input())
fact = 1

while n > 0:
    fact *= n
    n -= 1

print(fact)
