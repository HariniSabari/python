#q1
for i in range(5):
    print("Harinisabari")
#q2
for i in range(1, 21):
    print(i)
#q3
for i in range(20, 0, -1):
    print(i)
#q4
for i in range(2, 51, 2):
    print(i)    
#q5
for i in range(1,51,2):
    print(i)
#q6
sum=0
for i in range(1,11):
    sum+=i
    print("sum=",sum)
#q7
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#q8
name = input("Enter your name: ")
print("Number of letters:", len(name))
#q9
word = input("Enter a word: ")

for ch in word:
    print(ch)
#q10
word = input("Enter a word: ")

count = 0

for i in word:
    if i in "aeiouAEIOU":
        count = count + 1

print("Vowels =", count)
#q11        
n = 5

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#q12   

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
